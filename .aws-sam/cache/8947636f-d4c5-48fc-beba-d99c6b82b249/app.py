import json
import boto3
import datetime
import base64
import os
from aws_xray_sdk.core import patch
patch(['boto3'])

def lambda_handler(event, context):
    #
    #order = event["order"]
    order = { "orderId": "Mod9Demo","orderItem": "Donuts","quantity": "1", "receiptRequired": "true"}
    client = boto3.client('events')
    # 
    client.put_events(
        Entries=[{
            "Time": datetime.datetime.now(),
            "Source": "demo.eventbridge.order",
            "DetailType": "OrderCreated",
            "Resources": [
               order["orderId"]
            ],
            "Detail": json.dumps(order),
            "EventBusName": os.environ.get('EVENT_BUS')
        }]
    )
    #
    return {
        'statusCode': 200,
        'body': json.dumps('** The order event was issued **')
    }


