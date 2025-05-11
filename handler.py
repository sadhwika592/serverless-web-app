import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    body = json.loads(event['body'])
    item_id = body.get('id', str(datetime.utcnow().timestamp()))
    message = body.get('message', '')

    item = {
        'id': item_id,
        'message': message,
        'timestamp': datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item saved', 'item': item})
    }
