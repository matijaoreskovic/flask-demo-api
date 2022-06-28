FROM python:3.10.5-alpine

WORKDIR /app

RUN pip install flask

COPY ./app.py ./app.py

CMD [ "app.py" ]

ENTRYPOINT [ "python3" ]