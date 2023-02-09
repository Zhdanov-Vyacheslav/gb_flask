FROM python:3.8-alpine

COPY requirements.txt ./
COPY config_template.json ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app
COPY . .


EXPOSE 8000

#CMD flask run -h 0.0.0.0 -p 8000
CMD python run.py