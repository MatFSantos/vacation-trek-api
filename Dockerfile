FROM python:3.11.0

RUN pip install pipenv

RUN pip install prisma

WORKDIR /app

COPY . /app

RUN prisma migrate dev

RUN prisma generate

RUN pipenv install --deploy --system

EXPOSE 3333

CMD ["python", "run.py"]