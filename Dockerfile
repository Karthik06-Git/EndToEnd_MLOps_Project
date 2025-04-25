FROM python:3.11-slim-buster

RUN apt update -y && apt install awscli -y \
    && sed -i '/en_IN.UTF-8/s/^# //g' /etc/locale.gen \
    && locale-gen

ENV LANG en_IN.UTF-8  
ENV LANGUAGE en_IN:en  
ENV LC_ALL en_IN.UTF-8


WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]