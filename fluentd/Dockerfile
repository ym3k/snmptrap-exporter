FROM fluent/fluentd:v1.6-debian-1

USER root
ADD fluentd.conf /fluentd/etc/fluentd.conf

# RUN apt-get update && apt-get install -y make gcc && \
    # gem install fluent-plugin-mongo --no-document && \
    # apt-get remove -y make gcc && apt-get autoremove -y && apt-get autoclean -y
RUN apt-get update && \
    gem install fluent-plugin-influxdb --no-document
USER fluent
ENV FLUENTD_CONF=fluentd.conf

