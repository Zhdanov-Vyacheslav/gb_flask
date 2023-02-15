FROM python:3.8-alpine

COPY requirements.txt ./
COPY config_template.json ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app
COPY . .


EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 wsgi:app