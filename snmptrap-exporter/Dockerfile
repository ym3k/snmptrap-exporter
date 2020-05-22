FROM alpine:latest

RUN apk --no-cache add python3
RUN pip3 install prometheus_client influxdb
# RUN pip3 install prometheus_client pymongo influxdb

ADD exporter_influx.py /exporter/exporter.py

EXPOSE 8000

CMD ["python3","/exporter/exporter.py"]