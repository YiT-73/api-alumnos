import boto3
import json

def lambda_handler(event, context):
    data = json.loads(event['body'])
    tenant_id = data['tenant_id']
    alumno_id = data['alumno_id']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    response = table.get_item(Key={'tenant_id': tenant_id, 'alumno_id': alumno_id})
    item = response.get('Item')

    if item:
        return {
            'statusCode': 200,
            'body': json.dumps({'alumno': item})
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'mensaje': 'Alumno no encontrado'})
        }
