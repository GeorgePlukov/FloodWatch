import matplotlib.pyplot as plt
import time
import random
from collections import deque
import numpy as np
import datetime
from xbee import XBee,ZigBee
import serial
import time


a1 = deque([0]*100)
ax = plt.axes(xlim=(0, 20), ylim=(0, 10))

line, = plt.plot(a1,linewidth=4)
plt.ion()
plt.ylim([0,100])
plt.show()
PORT = 'your-serial-port'
BAUD_RATE = 9600

# Open serial port
print("about to open serial")
ser = serial.Serial(PORT, BAUD_RATE)

# This creates the graph and will redraw it based on new data that comes through the serial port
def runGraph(i):
    # Read a data point from the serial port, this reads 5 characters
    try:
      item = ser.read(5)
      float(item)
      # Add the item to the data list
      a1.appendleft(item)

    except ValueError:
        print ("not a float")
        return
      
    # Redraw the graph
    datatoplot = a1.pop()
    line.set_ydata(a1)
    plt.draw()
    plt.xlabel("Time Passed (Seconds)")
    plt.ylabel("Water Level (Meters)")
    plt.title("Dynamic Real Time Water Detection Disaster Preventer")
    t = datetime.datetime.now().time()

    i += 1
    time.sleep(0.01)
    plt.pause(0.000001)                


i = 0

while True:
    runGraph(i)
    i+=1
    
ser.close()
# file.close()
