# snmptrap-exporter
Export sum of snmptrap for Prometheus.

It seems that Prometheus and Grafana have been defact standard at network monitering,   
while 'snmptrap' is still used for traditional commercial network service infrastructure.

This snmptrap-exporter visualizes how many times and when snmptraps occured
in order to trace network unstabilities easily.

## how it works
InfluxDB or MongoDB stores snmptraps 

 {network deices}  -> snmptrap -> {snmptrapd} -> syslog -> {fluentd} -> db-plugin -> {influxdb/mongodb} 

Promethus scrape with snmptrap-exporter that counts traps occured within a fixed period.

## Requirement

* docker
* docker-compose

## how to use (instantly)
```
% docker-compose up 
```
default is MongoDB. 

## use InfluxDB
1. edit docker-compose.yaml, comment out mongo service and uncomment out influxdb.
1. edit fluend/fluent.conf, fix to use influxdb.
1. edit snmptrap-exporter/Dockerfile, comment-out.uncomment-out RUN&ADD block.

