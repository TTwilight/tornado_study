# -*- coding: utf-8 -*-
import sys
sys.path.append('./gen-py')
from hellow import HelloWorld
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost',9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol=TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloWorld.Client(protocol)
    transport.open()

    print 'client - ping '
    print 'server - '+client.ping()
    print 'client - say'
    msg=client.say('Hellow!')
    print 'server - '+msg
    transport.close()

except Thrift.TException as e:
    print e.message




