# Employee Data Publisher Lambda Function

This repository contains a Lambda function that processes HTTP requests containing employee data. The function validates the incoming data using Pydantic to ensure data integrity, generates a unique GUID for each message, and publishes the validated messages to an SQS queue.

---

## **How It Works**

1. **Input Validation**: 
   - Employee data is received in JSON format through an API Gateway.
   - Validation is performed using **Pydantic** to ensure the data adheres to the expected structure and constraints.

2. **GUID Generation**: 
   - A unique GUID is generated for each valid message.

3. **Message Publishing**: 
   - Valid messages are placed into an SQS queue for further processing.

4. **Error Handling**: 
   - If validation fails, an error response is returned, and details can be found in the CloudWatch logs.

---

## **Request Format**

The API Gateway expects HTTP POST requests with JSON payloads in the following format:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "EmployeeDetails": {
            "name": "John Doe",
            "employee_id": "1234",
            "local_address": {
                "apartment_number": "123",
                "street_name": "Main Street",
                "city_name": "Concord",
                "zip_code": "28027"
            }
        }
    }' \
  https://<API-GATEWAY-ENDPOINT>/dev/publish-message
