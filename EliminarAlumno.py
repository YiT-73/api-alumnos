import boto3
import json

def lambda_handler(event, context):
    data = json.loads(event['body'])
    tenant_id = data['tenant_id']
    alumno_id = data['alumno_id']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    table.delete_item(Key={'tenant_id': tenant_id, 'alumno_id': alumno_id})

    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': 'Alumno eliminado correctamente'})
    }