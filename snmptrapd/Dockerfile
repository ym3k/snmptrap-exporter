FROM alpine:latest

RUN apk --no-cache add net-snmp util-linux net-snmp-tools
#RUN echo 'disableAuthorization yes' > /etc/snmp/snmptrapd.conf
ADD snmp.conf /etc/snmp/snmp.conf
ADD snmptrapd.conf /etc/snmp/snmptrapd.conf
ADD nsswitch.conf /etc/nsswitch.conf

EXPOSE 8162/udp

CMD ["snmptrapd","-L","o","-f"]
