# FloodWatch
FloodWatch is a real time natural disaster early warning system. It provides simple and useful data over a wide area for researchers to track natural disaster events in real time and can serve as an early warning system in the hopes of saving lives. It was created for DeltaHacks 2 (Jan 2016) and won second place at the competition! 

<img src="winners.jpg" width="80%">


A large problem that current sensor networks have is that the data they collect is not easily accessable. Many times researchers will have to go out in the field to manually collect data from these devices before it is overwritten and lost. This is a very costly effort, however with floodwatch using radio transmission in a network allows all data to be piplined straight to a base station. This saves a lot of time and means no one will need to go into hazardous zones to collect data.

###How does Floodwatch work?
There are three main pieces to the FloodWatch system: Radio Transmision, Sensor arrays, and the software component. Each of these three pieces must work together flawlessy for FloodWatch to be able to accuratley and consistently provide information. 

####Radio Transmission
We chose to use radio transmission to transmit data because of its simplicity and how cost effective it is. Using XBee modules with a 6 - 8 Kilometer range, the sensor modules can be placed in a mesh network that will allow data to be routed back to the base station for hundereds of kilometers 