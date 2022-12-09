FROM python:3.10.7-slim

COPY ./app /api/app
COPY ./database.db /api
COPY ./main.py /api
COPY ./requirements.txt /api

WORKDIR /api

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]