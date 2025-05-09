FROM python:3.12

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
