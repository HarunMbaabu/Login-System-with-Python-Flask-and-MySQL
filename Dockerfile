FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*
COPY . .

RUN pip install mysqlclient
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python","main.py"]