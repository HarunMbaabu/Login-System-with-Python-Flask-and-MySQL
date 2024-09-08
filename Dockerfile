FROM python:3.8
RUN apt-get update
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]

FROM nginx
COPY