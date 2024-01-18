This Lambda function receives HTTP requests containing employee data in JSON format. It performs validation using data modeling modules like Pydantic to ensure the data's integrity. If the data is valid, it generates a unique GUID for each message and puts the message into an SQS queue.


....
