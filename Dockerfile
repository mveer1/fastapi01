FROM python:3.9

WORKDIR /docker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]

#run docker run -p 8000:8000 <name of the image, fastapi here>
#docker build -t fastapi .