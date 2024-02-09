This Lambda function receives HTTP requests containing employee data in JSON format. It performs validation using data modeling modules like Pydantic to ensure the data's integrity. If the data is valid, it generates a unique GUID for each message and puts the message into an SQS queue.
testing commit script 

The Request will be of below format will be sent to api gateway

curl -X POST   -H "Content-Type: application/json"   -d '{
    "EmployeeDetails": {
        "name": "dhfhffhf",
        "employee_id": "1234",
        "local_address": {
            "apartment_number": "123",
            "street_name": "1364647 ",
            "city_name": "concord",
            "zip_code": "28027"
        }
    }
}' https://*********.execute-api.eu-**north**-1.amazonaw**s.com/dev/*****-message



Sucsses Full Responce looks like this 

{
  "message": "All messages are placed in the queue"
}


If the employee data fails  at validation checks in publisher then  reponce will look like this 

{
  "message": "Error occured while placing messages in the queue please refer Cloud watch logs for more information"
}


we check the rows in the Dynamo DB will follow this structure 



<img width="719" alt="image" src="https://github.com/BhargaVNaiduV/publisher/assets/138513686/5477b5d1-977b-4244-96a1-3aaedfa0c105">

....
