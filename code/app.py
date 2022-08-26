import pandas as pd
import requests
import json

def wheather(event, context):

    first_name = event["first_name"]
    second_name = event["second_name"]
    message = event["message"]
    params = {
      'ippd': 'weather.com',
    }

    response = requests.get('https://securepubads.g.doubleclick.net/pagead/ppub_config', params=params)
    data = response.json()
    id = []
    for l in data[0][3]:
        id.append(l[1])

    df = pd.DataFrame(id)
    print(df)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f'{first_name},{second_name},{message}',
        }),
    }
