try:
    import json
    import os
    import boto3
    import logging
    import secrets
    import string
    import time
    from datetime import datetime
    from jinja2 import Environment, FileSystemLoader

    print("All modules are properly imported ...")

except Exception as e:
    print(f"Error Occurred While Importing Python Modules: {e}")

def employee_object_generater(EmployeeData):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('employee_template.j2')
    rendered_output = template.render(employee=EmployeeData)
    employee_dict = json.loads(rendered_output)
    return employee_dict

def lambda_handler(event, context):
    print(f"{datetime.now()} - Lambda function execution started.")
    print(f"{datetime.now()} - Please  find log details at below LOG Group Name,Log Stream Name " )
    employee_data = event.get("EmployeeDetails", {})
    #aws_data_source = event.get("aws_data_source", {})
    sqs_queue_url = os.environ.get('SQS_QUEUE_URL')

    try:
        sqs = boto3.client('sqs')
        start_time = time.time()

        message = employee_object_generater(employee_data)
        print(f"{datetime.now()} - The message we are sending right now is : {message}")
        
        response = sqs.send_message(QueueUrl=sqs_queue_url, MessageBody=json.dumps(message))
        
        print(f"{datetime.now()} - Message sent to the queue with url: {sqs_queue_url}")
        print(f"{datetime.now()} - Message sent to the queue. Response: {response}")

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"{datetime.now()} - Lambda function execution completed. Elapsed Time: {elapsed_time:.2f} seconds")

        result = {
            "message": "All messages are placed in the queue",
            "code": "200"
        }

        print(f"{datetime.now()} - Lambda function execution result: {json.dumps(result, indent=2)}")

        return result
    except Exception as e:
        print(f"{datetime.now()} - An error occurred: {str(e)}")
        return {
            "message": "ERROR : Please refer Cloudwatch logs for more Information",
            "code": "500"
        }
