FROM python:3.8
RUN apt-get update
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# It tells Docker to run your Flask application in a container so that it listens for incoming connections on all interfaces (0.0.0.0) at port 5000.
#This configuration allows external access to your Flask app.
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
