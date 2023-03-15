FROM python:3.9-buster

# Install Django
RUN apt-get update && cd goodline
RUN pip install venv && venv env
RUN env/bin/activate
RUN pip install -r requirements.txt

WORKDIR /goodline

# Start server
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["python3", "manage.py", "runserver"]