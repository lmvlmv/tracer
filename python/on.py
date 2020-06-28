#!/usr/bin/env python

import serial
from tracer import Tracer, TracerSerial, ManualCommand

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout = 1)
tracer = Tracer(0x16)
t_ser = TracerSerial(tracer, ser)
query = ManualCommand(True)
t_ser.send_command(query)
result = t_ser.receive_result()
# print "Raw bytes: %s" % ", ".join(map(lambda a: "%0X" % (a), result.data))
# print
# formatted = str(result).replace('{', '{\n')
# formatted = formatted.replace('}', '\n}')
# print formatted.replace(', ', '\n')