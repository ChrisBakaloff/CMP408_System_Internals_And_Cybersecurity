import datetime

import boto3
from boto3.dynamodb.conditions import Key , Attr
import json
import time
import sys

dynamo_client = boto3.client('dynamodb')
dyn_res = boto3.resource('dynamodb')

def get_items():
    date , time = get_date_time()
    table = dyn_res.Table('rpi_temp')
    print(date)
    res = table.query(
        KeyConditionExpression=Key('date').eq(date)
    )
    items = res['Items']
    print(items)
    return items



def get_date_time():
    dt = datetime.datetime.now()
    date = "{}-{}-{}".format(dt.day,dt.month, dt.year)
    time = "{}:{}:{}".format(dt.hour, dt.minute,dt.second)
    return date, time
 #Calculate date and time in format date - day-month-year , time - hours:minutes:seconds