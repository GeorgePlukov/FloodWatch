#! /usr/bin/python

"""
receive_samples.py

By Paul Malmsten, 2010
pmalmsten@gmail.com

This example continuously reads the serial port and processes IO data
received from a remote XBee.
"""

from xbee import XBee,ZigBee
import serial
import time

PORT = '/dev/tty.usbserial-00002014'
BAUD_RATE = 9600

# Open serial port
print("about to open serial")
ser = serial.Serial(PORT, BAUD_RATE)
ser.write('asd\r\n')
print("About to read line from serial")
for i in range (0,10):
	s = ser.read(4)
	print(s)
ser.close()