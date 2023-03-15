FROM python:3.10

WORKDIR /stuffaccounting_backend

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080" ]