import pymysql
import sys
import boto3
import os

ENDPOINT="database-3.cbuiroxadssw.us-east-1.rds.amazonaws.com"
PORT=3306
USER="admin"
PASSWORD="greet_team1"
REGION="us-east-1c"
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