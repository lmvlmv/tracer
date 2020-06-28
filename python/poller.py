import requests
import serial
from tracer import Tracer, TracerSerial, QueryCommand

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
devmap = {'charge_current', 7}


tracer = Tracer(0x16)
t_ser = TracerSerial(tracer, ser)
t_ser.send_command(QueryCommand())
result = t_ser.receive_result()

for dev in devmap:
    payload = {'type': 'command',
               'param': 'udevice',
               'idx': devmap[dev],
               'nvalue': 0,
               'svalue': getattr(result, dev)}

    r = requests.get('http://10.0.0.120:8080/json.htm', params=payload)
    print(r.json())
