#!/usr/bin/python2.7
from datetime import datetime
import serial,io

outfile='/tmp/serial-temperature.tsv'


ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate =9600,
)


#print help(io.TextIOWrapper)


sio  = io.TextIOWrapper(
    io.BufferedRWPair(ser,ser,1),
    encoding = 'ascii',newline = '\r'
)

with open(outfile, 'a') as f:
    while ser.isOpen():
        datastring = sio.readline()
        f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
        f.flush()

ser.close()    

