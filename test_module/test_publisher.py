import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
from your_lambda_module import lambda_handler  # Import your Lambda function

class TestLambdaFunction(unittest.TestCase):

    @patch('your_lambda_module.boto3.client')
    def test_lambda_handler_success(self, mock_boto3_client):
        # Mock SQS client
        mock_sqs_client = MagicMock()
        mock_boto3_client.return_value = mock_sqs_client

        # Mock event with valid data
        event = {
            "EmployeeDetails": {
                "name": "John Doe",
                "employee_id": 123,
                "local_address": {
                    "apartment_number": "A1",
                    "street_name": "Main St",
                    "city_name": "City",
                    "zip_code": 12345
                }
            }
        }

        # Call lambda_handler
        result = lambda_handler(event, None)

        # Assertions
        self.assertEqual(result["statusCode"], 200)
        self.assertIn("UUID", json.loads(result["body"]))

        # Ensure that the SQS client was called with the correct parameters
        mock_sqs_client.send_message.assert_called_with(
            QueueUrl='your_sqs_queue_url',
            MessageBody=MagicMock()  # Add the expected message body here
        )

    def test_lambda_handler_validation_error(self):
        # Mock event with invalid data to trigger validation error
        event = {
            "EmployeeDetails": {
                "name": "John Doe",
                "employee_id": "invalid_id",
                "local_address": {
                    "apartment_number": "A1",
                    "street_name": "Main St",
                    "city_name": "City",
                    "zip_code": 12345
                }
            }
        }

        # Call lambda_handler and catch the exception
        with self.assertRaises(ValueError):
            lambda_handler(event, None)

    def test_lambda_handler_input_validation_exception(self):
        # Mock event with data that will raise InputValidationException
        event = {
            "EmployeeDetails": {
                "name": "John Doe",
                "employee_id": 123,
                "local_address": {
                    "apartment_number": "A1",
                    "street_name": "Main St",
                    "city_name": "City",
                    "zip_code": "invalid_zip"
                }
            }
        }

        # Call lambda_handler and catch the exception
        with self.assertRaises(InputValidationException):
            lambda_handler(event, None)

if __name__ == '__main__':
    unittest.main()
