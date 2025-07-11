import boto3
import json

def lambda_handler(event, context):
    data = json.loads(event['body'])
    tenant_id = data['tenant_id']
    alumno_id = data['alumno_id']
    alumno_datos = data['alumno_datos']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    item = {
        'tenant_id': tenant_id,
        'alumno_id': alumno_id,
        'alumno_datos': alumno_datos
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': 'Alumno creado exitosamente', 'alumno': item})
    }