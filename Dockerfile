FROM ubuntu:16.04
COPY . /app
WORKDIR /app
RUN chmod +x entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]