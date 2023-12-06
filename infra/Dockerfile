FROM python:3.10-slim
WORKDIR /app
COPY /requirements.txt .
RUN apt update
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "shop.wsgi:application", "--bind", "0:8000" ]