FROM python:3.11.0

ENV PYTHONBUFFERRED=1
WORKDIR /Backend


RUN pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD [ "python", "manage.py", "runserver", "8000:8000" ]
