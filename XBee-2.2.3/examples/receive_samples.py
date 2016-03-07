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

PORT = '/dev/tty.usbserial-141'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)
print(ser.isOpen())
# Create API object
xbee = XBee(ser)

xbee.tx(
    dest_addr='\xFF\xFF',
    data="ur a dick")

# Continuously read and print packets
print ("eneter")
count = 0
while True:
  time.sleep(.5)
  print (count)
  xbee.tx(dest_addr='\x7F\xFF', data="ur a dick: {0}".format(count))
  count+=1




        
ser.close()
