import pandas as pd
import requests
import json
from sqlalchemy import create_engine
import sqlalchemy
from datetime import date, datetime, timedelta
import os

def wheather(event, context):

    begin = datetime.now()
    print(f"""
    ##############################################
    Start Time: {begin}
    """)

    first_name = event["first_name"]
    second_name = event["second_name"]
    message = event["message"]
    user = os.environ.get('USER')
    passwd = os.environ.get('PASSWORD')
    host = os.environ.get('HOST')
    port = os.environ.get('PORT')
    db = os.environ.get('DATABASE')

    # MySQL conection string.
    creds = {'user': user,
            'passwd': passwd,
            'host': host,
            'port': port,
            'db': db}
    connstr = 'mysql+mysqlconnector://{user}:{passwd}@{host}:{port}/{db}'
    mysql_conn = create_engine(connstr.format(**creds))
    # print(pd.read_sql_query(sql='SHOW TABLES', con=mysql_conn))

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
    print("Data Loaded Succesfully")

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
