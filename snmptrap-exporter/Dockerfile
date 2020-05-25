FROM alpine:latest

RUN apk --no-cache add python3 && \
    pip3 install prometheus_client pymongo
ADD exporter_mongo.py /exporter/exporter.py

# RUN apk --no-cache add python3 && \
#     pip3 install prometheus_client influxdb
# ADD exporter_influx.py /exporter/exporter.py

EXPOSE 8000

CMD ["python3","/exporter/exporter.py"]