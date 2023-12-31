from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymysql.cursors import DictCursor
from passlib.context import CryptContext
import uuid #to generate random userID's
from datetime import datetime, timedelta
from db_rds import ENDPOINT, PORT, USER, PASSWORD, DBNAME
from models import RegisterUserRequest, RequestEvent, Student, AcceptEvent #import pydantic models for routes
import pymysql


#conn =  pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, port=PORT, database=DBNAME, ssl_ca='./../../us-east-1-bundle.pem')
#cur = conn.cursor()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        "pass": register_request.password,
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

@app.get("/getUser")
async def getUser(email, password):
    #async def getUser(get_user_request: GetUserRequest):
    #return the userID and role 
    #print(query_results)
    #email = get_user_request.email
    #password = get_user_request.password
    queryUser = """SELECT userID, role FROM user WHERE email='""" + email + """' AND pass='""" + password + """'""" 

    try:
        conn = get_db_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute(queryUser)
                row = cur.fetchone()
                userID = row[0]
                role = row[1]
    except Exception as e:
        if conn.open:
            conn.rollback()
            conn.close()
        print("Error has occurred: ", e)
        raise HTTPException(status_code=500, detail=str(e))

    return {"userID": userID, "role": role}

@app.get("/getClass")
async def getClass(profID):
    #return the class members (list) and the time (date, 0-4, and start/end time)
    s = str(profID)
    queryClass = """SELECT classID, dayCode, startTime, endTime FROM class WHERE profID='""" + s + """'"""

    try:
        conn = get_db_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute(queryClass)
                row = cur.fetchone()
                classID = row[0]
                dayCode = row[1] #0-4 int
                startTime = row[2] #hh:mm:ss
                endTime = row[3] #hh:mm:ss
                s1 = str(classID)
                queryMembers = """SELECT studentID, email FROM user JOIN member ON user.userID=member.studentID WHERE classID='""" + s1 + """'""" 
                cur.execute(queryMembers)
                set = cur.fetchall() #set of all studentids for that class
                studentInfo=[]
                #studentIDs=[]
                for student in set:
                    #cur.execute(queryEmail)
                    pair = (student[0], student[1])
                    studentInfo.append(pair)
    except Exception as e:
        if conn.open:
            conn.rollback()
            conn.close()
        print("Error has occurred: ", e)
        raise HTTPException(status_code=500, detail=str(e))
    #day values 0-4 correspond to M-F; start and end times in format hh:mm:ss
    return {"classID": classID, "day": dayCode, "startTime": startTime, "endTime": endTime, "studentInfo":studentInfo}

@app.get("/getRequest")
async def getRequest(classID):
    s1 = str(classID)
    try:
        conn = get_db_connection()
        with conn:
            with conn.cursor() as cur:
                sql = """SELECT * FROM eventRequest WHERE classID='""" + s1 + """'"""
                cur.execute(sql)
                sqlReq = cur.fetchall()
                requests=[]
                for r in sqlReq:
                    classCode = r[0]
                    hsAdminID = r[1]
                    month = r[2]
                    day = r[3]
                    year = r[4]
                    tpl = (classCode,hsAdminID,month,day,year)
                    requests.append(tpl)
    except Exception as e:
        if conn.open:
            conn.rollback()
            conn.close()
        print("Error has occurred: ", e)
        raise HTTPException(status_code=500, detail=str(e))
    return requests

@app.post("/acceptRequest")
async def acceptRequest(accept_event: AcceptEvent):
     #insert this row into the confirmedEvent table, delete all records where classID=reqrequest.classID and hsAdminID=reqrequest.hsAdminID
    accepted_event = {
        "classID": accept_event.classID,
        "hsAdminID": accept_event.hsAdminID,
        "month": accept_event.month,
        "day": accept_event.day,
        "year": accept_event.year
    }

    try:
        conn = get_db_connection()
        with conn:
            with conn.cursor() as cur:
                sql = "INSERT INTO confirmedEvent(classID, hsAdminID, month, day, year) VALUES (%(classID)s, %(hsAdminID)s, %(month)s, %(day)s, %(year)s)"
                cur.execute(sql, accepted_event)
                #inserted, test delete
                s1 = str(accept_event.classID)
                s2 = str(accept_event.day)
                s3 = str(accept_event.month)
                s4 = str(accept_event.year)
                delsql = "DELETE FROM eventRequest WHERE classID='" + s1 + "' AND month='" + s2 + "' AND day='" + s3 + "' AND year='" + s4 + "'" 
                cur.execute(delsql)
    except Exception as e:
        if conn.open:
            conn.rollback()
            conn.close()
        print("Error has occurred: ", e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/getConfirmed")
async def getConfirmed(userID):
    #getconfirmed
    #query user based on userid, look at role
    s1 = str(userID)
    try:
        conn = get_db_connection()
        with conn:
            with conn.cursor() as cur:
                sql = """SELECT role FROM user WHERE userID='""" + s1 + """'"""
                cur.execute(sql)
                temp = cur.fetchone()
                var = temp
                if var == 0:
                    #student
                    sql = """SELECT classID FROM member WHERE studentID='""" + s1 + """'"""
                elif var == 1:
                    #college admin
                    sql = """SELECT classID FROM class WHERE profID='""" + s1 + """'"""
                else:
                    #hsadmin
                    sql = """SELECT classID FROM confirmedEvent WHERE hsAdminID='""" + s1 + """'"""
                cur.execute(sql)
                one = cur.fetchone()
                clid = one 
                s2 = str(clid)
                sql = """SELECT * FROM confirmedEvent WHERE classID='""" + s2 + """'"""
                set = cur.fetchall()
                confirmed=[]
                for r in set:
                    classCode = r[0]
                    hsAdminID = r[1]
                    month = r[2]
                    day = r[3]
                    year = r[4]
                    tpl = (classCode,hsAdminID,month,day,year)
                    confirmed.append(tpl)
    except Exception as e:
        if conn.open:
            conn.rollback()
            conn.close()
        print("Error has occurred: ", e)
        raise HTTPException(status_code=500, detail=str(e))
    return confirmed
    

    

#@app.post("/loginHSAdmin")
#async def loginHSAdmin():
#    return True

#@app.post("/loginCollegeAdmin")
#async def loginCollegeAdmin():
#    return False

#conn = databaseCOnnection

def authenticate_user(email, password):
    with get_db_connection() as conn:
        with conn.cursor(DictCursor) as cur:  
            sql_statement = "SELECT userid, email, pass, role FROM user WHERE email = %s"
            cur.execute(sql_statement, (email,))
            user_record = cur.fetchone()

            if user_record and pwd_context.verify(password, user_record['pass']):
                return {
                    "userid": user_record['userid'],
                    "email": user_record['email'],
                    "role": user_record['role']
                }
            else:
                return None

@app.post("/requestEvent")
async def request_event(request_event: RequestEvent):
    # user = authenticate_user(request_event.email, request_event.password) #method to determine correct user
    # if not user:
    #     raise HTTPException(status_code=405, detail="user does not exist")

    # if user['role'] != 2:
    #     raise HTTPException(status_code=404, detail="person is not the right role")

    # class_id = 2 #HARD CODED for now

    # if not class_id:
    #     raise HTTPException(status_code=404, detail="Class not found for this admin")

    new_calendar_event = {
        "classID": request_event.classID,
        "hsAdminID": request_event.hsAdminID,
        "Day": request_event.day,
        "Month": request_event.month,
        "Year": request_event.year
    }
    print(new_calendar_event)
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                sql_request_statement = """INSERT INTO eventRequest (classID, hsAdminID, Day, Month, Year)
                                           VALUES (%(classID)s, %(hsAdminID)s, %(Day)s, %(Month)s, %(Year)s)"""
                cur.execute(sql_request_statement, new_calendar_event)
                conn.commit()
        return {"message": "Event requested successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get_all_classes")
async def get_all_classes(day_code: int):
    if day_code not in range(5):
        raise HTTPException(status_code=400, detail="Invalid DayCode supplied")

    today = datetime.today()
    first_day_next_month = (today.replace(day=1) + timedelta(days=31)).replace(day=1)
    
    first_weekday = first_day_next_month.weekday()

    day_difference = (day_code - first_weekday) % 7
    first_class_day = first_day_next_month + timedelta(days=day_difference)

    class_dates = []
    while first_class_day.month == first_day_next_month.month:
        class_dates.append(first_class_day)
        first_class_day += timedelta(days=7)
    print(class_dates)
    classes_list = []
    try:
        with get_db_connection() as conn:
            with conn.cursor(DictCursor) as cur:
                for class_date in class_dates:
                    sql_statement = """SELECT * FROM class 
                                       WHERE DayCode = %s""" 
                    cur.execute(sql_statement, (day_code,))
                    classes = cur.fetchall()
                    for class_meeting in classes:
                        class_meeting['month'] = class_date.month-1
                        class_meeting['day'] = class_date.day
                        class_meeting['year'] = class_date.year
                    classes_list.extend(classes)
        return classes_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#TODO
app.post('/acceptRequest')
async def acceptRequest():
    return True

app.post('/denyRequest')
async def denyRequest():
    return True

@app.get("/getAllStudents")
async def get_all_students():
    unassigned_students = []
    try:
        with get_db_connection() as conn:
            with conn.cursor(DictCursor) as cur:
                sql_statement = """
                SELECT user.userid, user.email FROM user
                LEFT JOIN member ON user.userid = member.studentID
                WHERE user.role = 0 AND member.classID IS NULL
                """
                cur.execute(sql_statement)
                unassigned_students_records = cur.fetchall()
                unassigned_students = [Student(**record) for record in unassigned_students_records]
        return unassigned_students
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))