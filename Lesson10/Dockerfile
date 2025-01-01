FROM python:3.11
WORKDIR /webapp
COPY . /webapp
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]


# docker build --platform linux/amd64 -t gde-devops:latest .