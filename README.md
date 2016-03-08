# FloodWatch
FloodWatch is a real time natural disaster early warning system. It provides simple and useful data over a wide area for researchers to track natural disaster events in real time and can serve as an early warning system in the hopes of saving lives. It was created for DeltaHacks 2 (Jan 2016) and won second place at the competition! 

<img src="winners.jpg" width="80%">


A large problem that current sensor networks have is that the data they collect is not easily accessable. Many times researchers will have to go out in the field to manually collect data from these devices before it is overwritten and lost. This is a very costly effort, however with floodwatch using radio transmission in a network allows all data to be piplined straight to a base station. This saves a lot of time and means no one will need to go into hazardous zones to collect data.

###How does Floodwatch work?
There are three main pieces to the FloodWatch system: Radio Transmision, Sensor arrays, and the software component. Each of these three pieces must work together flawlessy for FloodWatch to be able to accuratley and consistently provide information. 

##### Radio Transmission
We chose to use radio transmission to transmit data because of its simplicity and how cost effective it is. Using XBee modules with a 6 - 8 Kilometer range, the sensor modules can be placed in a mesh network that will allow data to be routed back to the base station for hundereds of kilometers. Another benefit to these is that they only cost aroun $30 at a consumer price level which makes the modules fairly affordable. 

##### Sensor Arrays
The sensor arrays are controlled by an arduino and can allow any sensor to be attached to it. Anything from thermometers to seismometers to buoancy meters can be attatched depending on the area the devices are going to be deployed to. The Arduino will be controlling the XBee and the sensors which makes it very simple to send data back and forth. The power consumption is also fairly low which means that a battery could last a long time, or a small solar panel would be enough to keep the power flowing. 

##### Base Module/Software component
The base module is simply a computer that will allow all the data read by the sensor arrays to be collected at one station. This is currently a fairly basic program that will take all of the data that is read through the XBee module and will graph and record it. This also can be designed depending on what the sensor data needs to represent. 

