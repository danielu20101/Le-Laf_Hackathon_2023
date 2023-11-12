from fastapi import FastAPI, Depends, Request, HTTPException

from passlib.context import CryptContext
import uuid #to generate random userID's

from db_rds import ENDPOINT, PORT, USER, PASSWORD, DBNAME
from models import RegisterUserRequest #our model to register a user

import pymysql


conn =  pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, port=PORT, database=DBNAME, ssl_ca='./../../us-east-1-bundle.pem')
cur = conn.cursor()




app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Test Successful"}


def get_db_connection():
    return pymysql.connect(
        host=ENDPOINT, 
        user=USER, 
        passwd=PASSWORD, 
        port=PORT, 
        database=DBNAME, 
        ssl_ca='./../../us-east-1-bundle.pem'
    )

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
minPasswordLen = 8 #minimum password length
@app.post("/registerUser")
async def register_user(register_request: RegisterUserRequest):
    if len(register_request.password) < minPasswordLen:
        raise HTTPException(status_code=400, detail="Password should be at least 8 characters long")

    hashed_password = pwd_context.hash(register_request.password)
    user_id = str(uuid.uuid4())  # Generate a new UUID for the userID

    new_user = {
        "userid": user_id,
        "email": register_request.email,
        "pass": hashed_password,
        "role": register_request.role
    }

    sql_statement = "INSERT INTO user (userID, email, pass, role) VALUES (%(userid)s, %(email)s, %(pass)s, %(role)s)"

    try:
        conn = get_db_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql_statement, new_user)
                conn.commit()
    except Exception as e:
        if conn.open:
            conn.rollback()
            conn.close()
        print("Error has occurred: ", e)
        raise HTTPException(status_code=500, detail=str(e))

    return {"userID": user_id, "message": "User registered successfully"}


#@app.post("/loginHSAdmin")
#async def loginHSAdmin():
#    return True

#@app.post("/loginCollegeAdmin")
#async def loginCollegeAdmin():
#    return False

#conn = databaseCOnnection