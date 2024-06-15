GET START

REPOSITORY: https://github.com/DmytroPavlikoskiy/FastAPITask

Command:

mkdir project

cd project

git clone <REPOSITORY>

docker-compose up --build


REGISTER:

"https://domen.com/register_user/"

Method: POST

JSON_REQUEST: {

    "username": username,
    "password", password,

}

TEST_MODE_JSON_REQUEST: {

    "username": username,
    "password", password,
    "role": role(default role "user")

}

In the test mode, you can set to enter both the manager and the admin.

LOGIN

"https://domen.com/login/"

Method: POST

JSON_REQUEST: {

    "username": username,
    "password", password,

}

JSON_RESPONSE: {

    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJUZXN0MSIsImV4cCI6MTcxODQ1NTEwNH0.yrNXsRaE1d0d95_1R_EU68TyBPk4hSECfaMOQsdHDGo",
    "token_type": "bearer"

}

GET DATA FOR TELEGRAM MESSAGE

"https://domen.com/get_and_save_data/"

Method: POST

JSON_REQUEST: {

    "bot_token": "6503074282:PAGwvcfDGyXJKASzAU72uDIULmRZesOygBo",
    "chat_id": "7128321519",
    "message": "Hello World"

}

JSON_RESPONSE:{

    "status": "success"

}

GET RECORD

"https://domen.com/record/1"

Method: GET

JSON_RESPONSE: {

    "id": 1,
    "username": "Test1",
    "bot_token": "6503074282:AAGwvcfDGyXJKASzAU72uDIULmRZesOygBo",
    "message": "Макс Лох",
    "user_role": "user",
    "user_id": 1,
    "chat_id": "7128321509",
    "telegram_response":"{\"ok\": true, \"result\": {\"message_id\": 5,
    \"from\": {\"id\": 6503074282, \"is_bot\": true, \"first_name\": \"iditenahuybot\",
    \"username\": \"ItitdeNahuyBot\"}, \"chat\": {\"id\": 7128321509, \"first_name\": \"\Д\м\и\т\р\о\",
    \"username\": \"wizex375\", \"type\": \"private\"}, \"date\": 1718447164,
    \"text\": \"\H\e|l|l|o"}}"

}

GET ALL RECORDS

"https://domen.com/users/1/records"

Method: GET


JSON_RESPONSE: [

    {
        "user_id": 1,
        "user_role": "user",
        "chat_id": "7128321509",
        "telegram_response":"{\"ok\": true, \"result\": {\"message_id\": 8, \"from\": {\"id\": 6503074282, \"is_bot\": true, \"first_name\": \"iditenahuybot\", \"username\": \"ItitdeNahuyBot\"}, \"chat\": {\"id\": 7128321509, \"first_name\": \"\Д\м\и\т\р\о\", \"username\": \"wizex375\", \"type\": \"private\"}, \"date\": 1718453317, \"text\": \"Hello World\"}}",
        "username": "Test1",
        "id": 1,
        "bot_token": "6503074282:AAGwvcfDGyXJKASzasU72uDIULmRZesOygBo",
        "message": "Hello World"
    },

    {
        "user_id": 2,
        "user_role": "user",
        "chat_id": "7128321609",
        "telegram_response":"{\"ok\": true, \"result\": {\"message_id\": 8, \"from\": {\"id\": 6503074282, \"is_bot\": true, \"first_name\": \"iditenahuybot\", \"username\": \"ItitdeNahuyBot\"}, \"chat\": {\"id\": 7128321509, \"first_name\": \"\Д\м\и\т\р\о\", \"username\": \"wizex375\", \"type\": \"private\"}, \"date\": 1718453317, \"text\": \"Hello World\"}}",
        "username": "Test2",
        "id": 2,
        "bot_token": "6503074282:AAGwvbdfDGyXJKASzAU72uDIULmRZesOygBo",
        "message": "Hello World"
    }
]