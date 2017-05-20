From python
MAINTAINER X4mp

RUN mkdir /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY server.py /app

EXPOSE 3000

WORKDIR /app

ENTRYPOINT ["python", "app.py"]
