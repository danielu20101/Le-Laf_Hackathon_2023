import pymysql
import sys
import boto3
import os
import pathlib
import csv

ENDPOINT="database-3.cbuiroxadssw.us-east-1.rds.amazonaws.com"
PORT=3306
USER="admin"
PASSWORD="greet_team1"
#REGION="us-east-1c"
DBNAME="greet_db"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
#session = boto3.Session(profile_name='default')
#client = session.client('rds')

#token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn =  pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, port=PORT, database=DBNAME, ssl_ca='./../../us-east-1-bundle.pem')
    cur = conn.cursor()
    #cur.execute("""SELECT now()""")
    #query_results = cur.fetchall()
    #print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e)) 

cur = conn.cursor()
#cur.execute("""SELECT now()""")
#query_results = cur.fetchall()
#print(query_results)

for arg in sys.argv:
    if arg == "-c":
        ##DDL CREATE, (create top-level down based on referential dependencies)
        createUser = """CREATE TABLE user (userID INT AUTO_INCREMENT, email VARCHAR(255), pass VARCHAR(255), role INT, CHECK (role>=0 AND role <=2), PRIMARY KEY (userID))"""
        cur.execute(createUser)
        createClass = """CREATE TABLE class (classID INT AUTO_INCREMENT, profID INT, dayCode INT, startTime TIME, endTime TIME, CHECK (dayCode>=0 AND dayCode <=4), PRIMARY KEY (classID, profID), FOREIGN KEY (profID) REFERENCES user(userID))"""
        cur.execute(createClass)
        createMember = """CREATE TABLE member (classID INT, studentID INT, PRIMARY KEY (classID, studentID), FOREIGN KEY (classID) REFERENCES class(classID), FOREIGN KEY (studentID) REFERENCES user(userID))"""
        cur.execute(createMember)
        createEventRequest = """CREATE TABLE eventRequest (classID INT, hsAdminID INT, month INT, day INT, year INT, CHECK(month >= 1 AND month <=12), CHECK(day>=1 AND day<=31), CHECK(year>=1900 AND year<=2100), PRIMARY KEY (classID, hsAdminID, month, day, year), FOREIGN KEY (classID) REFERENCES class(classID), FOREIGN KEY (hsAdminID) REFERENCES user(userID))"""
        cur.execute(createEventRequest)
        createConfirmedEvent = """CREATE TABLE confirmedEvent (classID INT, hsAdminID INT, month INT, day INT, year INT, CHECK(month >= 1 AND month <=12), CHECK(day>=1 AND day<=31), CHECK(year>=1900 AND year<=2100), PRIMARY KEY (classID, hsAdminID, month, day, year), FOREIGN KEY (classID) REFERENCES class(classID), FOREIGN KEY (hsAdminID) REFERENCES user(userID))"""
        cur.execute(createConfirmedEvent)
        #all tables created
    elif arg == "-d":
        ##DDL DROP, (delete from bottom-up based on weakest dependencies)
        dropConfirmedEvent = """DROP TABLE confirmedEvent"""
        cur.execute(dropConfirmedEvent)
        dropEventRequest = """DROP TABLE eventRequest"""
        cur.execute(dropEventRequest)
        dropMember = """DROP TABLE member"""
        cur.execute(dropMember)
        dropClass = """DROP TABLE class"""
        cur.execute(dropClass)
        dropUser = """DROP TABLE user"""
        cur.execute(dropUser)
        #all tables dropped
        #chsange the csv paths
    elif arg == "-z":
        #insert users
        csv_path = pathlib.Path.cwd() / "./staticCSV/user.csv"
        dict_list = list()
        with csv_path.open(mode="r") as csv_reader:
            csv_reader = csv.reader(csv_reader)
            for rows in csv_reader:
                dict_list.append({'userID':rows[0], 'email':rows[1], 'pass':rows[2], 'role': rows[3]})
        for item in dict_list:
            sql = "INSERT INTO user(userID, email, pass, role) VALUES (%s, %s, %s, %s)"
            val = item['userID'], item['email'], item['pass'], item['role']
            cur.execute(sql, val)
    elif arg == "-b":
        #insert classes 
        csv_path = pathlib.Path.cwd() / "./staticCSV/class.csv"
        dict_list = list()
        with csv_path.open(mode="r") as csv_reader:
            csv_reader = csv.reader(csv_reader)
            for rows in csv_reader:
                dict_list.append({'profID':rows[0], 'dayCode':rows[1], 'startTime':rows[2], 'endTime': rows[3]})
        for item in dict_list:
            sql = "INSERT INTO class(profID, dayCode, startTime, endTime) VALUES (%s, %s, %s, %s)"
            val = item['profID'], item['dayCode'], item['startTime'], item['endTime']
            cur.execute(sql, val)
    elif arg == "-m":
        #insert members
        csv_path = pathlib.Path.cwd() / "./staticCSV/member.csv"
        dict_list = list()
        with csv_path.open(mode="r") as csv_reader:
            csv_reader = csv.reader(csv_reader)
            for rows in csv_reader:
                dict_list.append({'classID':rows[0], 'studentID':rows[1]})
        for item in dict_list:
            sql = "INSERT INTO member(classID, studentID) VALUES (%s, %s)"
            val = item['classID'], item['studentID']
            cur.execute(sql, val)
    elif arg == "-e":
        #insert eventRequests
        csv_path = pathlib.Path.cwd() / "data.csv"
        dict_list = list()
        with csv_path.open(mode="r") as csv_reader:
            csv_reader = csv.reader(csv_reader)
            for rows in csv_reader:
                dict_list.append({'userID':rows[0], 'email':rows[1], 'pass':rows[2], 'role': rows[3]})
    elif arg == "-k":
        #insert confirmed events
        csv_path = pathlib.Path.cwd() / "data.csv"
        dict_list = list()
        with csv_path.open(mode="r") as csv_reader:
            csv_reader = csv.reader(csv_reader)
            for rows in csv_reader:
                dict_list.append({'userID':rows[0], 'email':rows[1], 'pass':rows[2], 'role': rows[3]})
        
conn.commit()
str = """SELECT userID FROM user"""
cur.execute(str)
test = cur.fetchall()
print(test)

#define routes