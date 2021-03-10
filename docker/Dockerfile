FROM python:3.6

WORKDIR /app

ENV FILENAME=""

COPY . .

RUN pip install git+https://github.com/reclada/connector.git &&\
    pip install .

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD [ "python", "job" ]
