FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /docker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]
