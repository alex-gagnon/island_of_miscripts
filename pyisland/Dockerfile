FROM python:3

WORKDIR /app

COPY ./setup.py ./
COPY ./requirements.txt ./
RUN pip install --no-cache -r requirements.txt
RUN pip install -e .

COPY . .

CMD ["pytest"]
