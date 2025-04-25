FROM python:3.11-slim-buster

RUN apt update -y && \
    apt install  locales awscli -y && \
    echo "en_IN.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_IN.UTF-8 && \
    update-locale LANG=en_IN.UTF-8

# Set environment variables for locale
ENV LANG=en_IN.UTF-8  
ENV LANGUAGE=en_IN:en  
ENV LC_ALL=en_IN.UTF-8


WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]