#!/usr/bin/python
import time
import PyDragonfly
from PyDragonfly import copy_from_msg
import message_defs as mdefs
import sys

MID_CONSUMER = 11

# Note: Consumer must be started second

if __name__ == "__main__":
    mod = PyDragonfly.Dragonfly_Module(MID_CONSUMER, 0)
    mod.ConnectToMMM()
    mod.Subscribe(mdefs.MT_TEST_DATA)
    mod.SendModuleReady()
    
    print "Consumer running...\n"
    
    for i in range(10):
        msg = PyDragonfly.CMessage()
        mod.ReadMessage(msg)    # blocking read
        print "Received message", msg.GetHeader().msg_type
        if msg.GetHeader().msg_type == mdefs.MT_TEST_DATA:
            msg_data = mdefs.MDF_TEST_DATA()
            copy_from_msg(msg_data, msg)
            print "Data = [a: %d, b: %d, x: %f]" % (msg_data.a, msg_data.b, msg_data.x)
        
    mod.DisconnectFromMMM()
        