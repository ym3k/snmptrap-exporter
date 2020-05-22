FROM alpine:latest

RUN apk --no-cache add python3 vim
RUN pip3 install prometheus_client 
# RUN pip3 install prometheus_client pymongo influxdb

ADD exporter.py /exporter/exporter.py

EXPOSE 8000

CMD ["python3","/exporter/exporter.py"]
