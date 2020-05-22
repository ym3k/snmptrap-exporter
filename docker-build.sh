docker build -t snmptrap-exporter/snmptrapd:v1 snmptrapd
docker build -t snmptrap-exporter/snmptrap-exporter:v1 snmptrap-exporter
docker build -t snmptrap-exporter/fluentd:v1 fluentd
docker build -t snmptrap-exporter/prometheus:v1 prometheus

docker tag snmptrap-exporter/snmptrapd:v1 harbor.mnj.pfn.io/cluster-services/switch-snmp-snmptrapd:v1
docker push harbor.mnj.pfn.io/cluster-services/switch-snmp-snmptrapd:v1

docker tag snmptrap-exporter/snmptrap-exporter:v1 harbor.mnj.pfn.io/cluster-services/switch-snmp-snmptrap-exporter:v1
docker push harbor.mnj.pfn.io/cluster-services/switch-snmp-snmptrap-exporter:v1

docker tag snmptrap-exporter/fluentd:v1 harbor.mnj.pfn.io/cluster-services/switch-snmp-fluentd:v1
docker push harbor.mnj.pfn.io/cluster-services/switch-snmp-fluentd:v1

docker tag snmptrap-exporter/prometheus:v1 harbor.mnj.pfn.io/cluster-services/switch-snmp-prometheus:v1
docker push harbor.mnj.pfn.io/cluster-services/switch-snmp-prometheus:v1
