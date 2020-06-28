#!/usr/bin/env python

import serial
from tracer import Tracer, TracerSerial, QueryCommand

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout = 1)

tracer = Tracer(0x16)
t_ser = TracerSerial(tracer, ser)
query = QueryCommand()
t_ser.send_command(query)
result = t_ser.receive_result()

print "Charge: {}".format(result.charge_current)
