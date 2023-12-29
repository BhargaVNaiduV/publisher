FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
CMD ["lambda_publisher_function.lambda_handler"]
