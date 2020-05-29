from pysnmp.hlapi import *

IfHCInOctets = '.1.3.6.1.2.1.31.1.1.1.6'
ifHCOutOctets = '.1.3.6.1.2.1.31.1.1.1.7'
community = 'public!public'
targetip = '192.168.27.100'

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          CommunityData(community),
                          UdpTransportTarget(('192.168.27.100')),
                          ContextData(),
                          ObjectType(ObjectIdentity(IfHCInOctets)),
                          ObjectType(ObjectIdentity(ifHCOutOctets)),
                          lexicographicMode=False):

    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))