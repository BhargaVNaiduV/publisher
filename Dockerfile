FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY lambda_publisher_function.py ./
COPY employee_template.j2 ./
CMD ["lambda_publisher_function.lambda_handler"]
