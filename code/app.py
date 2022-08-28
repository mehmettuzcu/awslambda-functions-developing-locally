import pandas as pd
import requests
import json
import os
import boto3
import sqlalchemy

from sqlalchemy import create_engine
from boto3.session import Session
from datetime import date, datetime, timedelta


def wheather(event, context):

    begin = datetime.now()
    print(f"""
    ##############################################
    Start Time: {begin}
    """)

    # Environment variables
    first_name = event["first_name"]
    second_name = event["second_name"]
    message = event["message"]
    user = os.environ.get('USER')
    passwd = os.environ.get('PASSWORD')
    host = os.environ.get('HOST')
    port = os.environ.get('PORT')
    db = os.environ.get('DATABASE')
    access_key = os.environ.get('ACCESS_KEY')
    secret_key = os.environ.get('SECRET_KEY')
    bucket_name = os.environ.get('BUCKET_NAME')

    # MySQL conection string.
    creds = {'user': user,
            'passwd': passwd,
            'host': host,
            'port': port,
            'db': db}
    connstr = 'mysql+mysqlconnector://{user}:{passwd}@{host}:{port}/{db}'
    mysql_conn = create_engine(connstr.format(**creds))
    # print(pd.read_sql_query(sql='SHOW TABLES', con=mysql_conn))

    # S3
    session = Session(aws_access_key_id=access_key,
                  aws_secret_access_key=secret_key)
    s3 = session.resource('s3')
    bucket = s3.Bucket(bucket_name)

    params = {
      'ippd': 'weather.com',
    }
    response = requests.get('https://securepubads.g.doubleclick.net/pagead/ppub_config', params=params)
    data = response.json()

    id = []
    for l in data[0][3]:
        id.append(l[1])

    df = pd.DataFrame(id)
    df.to_sql(name='wheatherId',con=mysql_conn, index=False, if_exists='replace')
    print("Data Loaded Succesfully to MySQL")

    """df.to_csv("wheather.csv", index=False)
    local_path = './wheather.csv'
    bucket_path = 'tuzcu2/wheather.csv'
    s3.meta.client.upload_file(Filename=local_path, Bucket=bucket_name, Key=bucket_path)

    print("Data Loaded Succesfully to MySQL")"""

    end = datetime.now()
    print(f"""
    Finished Time: {end}
    Total Time: {end - begin}    
    ##################################################    
        """)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f'{first_name},{second_name},{message}',
        }),
    }
