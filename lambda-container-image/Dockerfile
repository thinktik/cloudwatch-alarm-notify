FROM public.ecr.aws/lambda/python:3.8

# 主要维护人员
MAINTAINER ThinkTik <thinktik@outlook.com>

#RUN pip install awslambdaric

COPY src/hello_container.py ./
CMD ["hello_container.lambda_handler"]