FROM python
RUN mkdir /nordic
RUN chmod 777 /nordic
COPY . /nordic
WORKDIR /nordic
RUN pip install -r requirements.txt
CMD ["python", "app.py"]