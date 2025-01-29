FROM python:3.12

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libffi-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app

CMD ["sh", "-c", "alembic upgrade head && python3 -u main.py"]