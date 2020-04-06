FROM alpine:latest

RUN apk --no-cache add net-snmp util-linux
#RUN echo 'disableAuthorization yes' > /etc/snmp/snmptrapd.conf
RUN echo 'mibs all' > /etc/snmp/snmp.conf
ADD snmptrapd.conf /etc/snmp/snmptrapd.conf

EXPOSE 162/udp

CMD ["snmptrapd","-L","o","-f"]
