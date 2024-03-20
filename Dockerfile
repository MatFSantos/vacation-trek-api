FROM python:3.11.0

RUN pip install pipenv

WORKDIR /app

COPY . /app

RUN pipenv install --deploy --system

EXPOSE 3333

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

CMD ["/usr/local/bin/entrypoint.sh"]
