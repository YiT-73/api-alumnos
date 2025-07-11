import boto3
import json

def lambda_handler(event, context):
    data = json.loads(event['body'])
    tenant_id = data['tenant_id']
    alumno_id = data['alumno_id']
    nuevos_datos = data['alumno_datos']  # Dict con campos a modificar

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    update_expression = []
    expression_values = {}

    for clave, valor in nuevos_datos.items():
        update_expression.append(f'alumno_datos.{clave} = :{clave}')
        expression_values[f':{clave}'] = valor

    table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression='SET ' + ', '.join(update_expression),
        ExpressionAttributeValues=expression_values
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': 'Alumno actualizado correctamente'})
    }