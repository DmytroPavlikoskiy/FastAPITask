from sqlalchemy.orm import Session


def get_or_create(db: Session, model, **kwargs):
    instance = db.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = {**kwargs}
        instance = model(**params)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance, True


def get_obj(db: Session, model, **kwargs):
    obj = db.query(model).filter_by(**kwargs).first()
    if not obj:
        return obj, False
    return obj