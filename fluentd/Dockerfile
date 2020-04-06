FROM fluent/fluentd:v1.6-debian-1

USER root

RUN apt-get update && apt-get install -y make gcc

ADD fluentd.conf /fluentd/etc/fluentd.conf

RUN ["gem", "install", "fluent-plugin-mongo", "--no-document"]
USER fluent
ENV FLUENTD_CONF=fluentd.conf

