import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    data = json.loads(json.dumps(event))
    payload = data['data']
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
                                       
    goal = json.loads(response['Body'].read().decode())


    s_value = float(goal)
    p_value = f"Prediction of {data} is : "


    if s_value == 1.0:
        p_value += 'versicolor'
    elif s_value == 0.0:
        p_value += 'setosa'
    else:
        p_value += 'virginica'
    
    print("Predicted Result : ", p_value)
    
    return p_value