import json

from fastapi import FastAPI, Depends, HTTPException, status
from . import schemas, auth
from .models import User, Record
from .schemas import *
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import requests
from .dependencies import get_db
from .schemas import MessageRequest
from .database import engine, Base

from .services import get_or_create, get_obj


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/register_user/")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """ Register a new user """
    try:
        hashed_password = auth.get_password_hash(user.password)

        """ Uncomment before release """
        # if user.role in ["admin", "manager"]:
        #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Sorry, you cannot give yourself a role")

        user_data = {
            "username": user.username,
            "password": hashed_password,
            "role": user.role
        }

        try:
            new_user, created = get_or_create(db, User, **user_data)
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

        if created:
            return {"data": {"new_user": new_user.username, "user_role": new_user.role}, "success": True}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    except Exception as ex:
        print(ex)
        return {"data": {"error": "error", "message": "Something wrong"}}


@app.post("/login/")
def login_user(user_data: LoginUsers, db: Session = Depends(get_db)):
    """ Authorization and JWT token issuance """

    user = get_obj(db, User, username=user_data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not auth.verify_password(user_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/get_and_save_data/")
def get_and_save_data(data: MessageRequest,current_user: User = Depends(auth.get_current_active_user), db: Session = Depends(get_db)):
    """ Receiving telegrams of JSON data, processing, and saving """

    message = {
        'user_id': current_user.id,
        'username': current_user.username,
        'user_role': current_user.role,
        'bot_token': data.bot_token,
        'chat_id': data.chat_id,
        'message': data.message
    }
    db_message, created = get_or_create(db, Record, **message)
    if created:
        send_tel_message(db=db, record_id=db_message.id)
    else:
        send_tel_message(db=db, record_id=db_message.id)

    return {"status": "success"}


def send_tel_message(db, record_id):
    """ Sending a message to Telegram, and saving a response from the Telegram API """
    record_id = {"id": record_id}
    record = get_obj(db, Record, **record_id)
    url = f"https://api.telegram.org/bot{record.bot_token}/sendMessage"
    payload = {
        "chat_id": record.chat_id,
        "text": record.message
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to send message")

    response_data = response.json()
    record.telegram_response = json.dumps(response_data)
    db.commit()


@app.get("/record/{record_id}")
async def read_record(record_id: int, current_user: User = Depends(auth.get_current_active_user), db: Session = Depends(get_db)):
    """ Get the record according to the user rule """
    db_record = db.query(Record).filter(Record.id == record_id).first()
    if db_record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    if db_record.user_id != current_user.id and current_user.role not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    if current_user.role == "manager":
        manager_users = db.query(User).filter(User.id == db_record.user_id, User.role == "user").all()
        if not manager_users:
            raise HTTPException(status_code=403, detail="Not enough permissions")
    return db_record


@app.get("/users/{user_id}/records")
async def get_user_records(user_id: int, current_user: User = Depends(auth.get_current_active_user), db: Session = Depends(get_db)):
    """ Get all user records. Verification according to user role """
    if current_user.role == "user" and current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    if current_user.role == "manager":
        manager_users = db.query(User).filter(User.id == user_id, User.role == "user").all()
        if not manager_users:
            raise HTTPException(status_code=403, detail="Not enough permissions")
    records = db.query(Record).filter(Record.user_id == user_id).all()
    return records




