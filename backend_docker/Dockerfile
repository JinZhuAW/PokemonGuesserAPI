FROM python:3.8

# set working directory
WORKDIR /app

COPY . ./

RUN pip install --upgrade --no-cache-dir -r ./requirements.txt
ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]