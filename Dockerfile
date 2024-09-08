FROM python:3.8
RUN apt-get update
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
