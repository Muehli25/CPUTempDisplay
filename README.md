# CPUTempDisplay

A small arduino Project

## Hardware

- Arduino Uno or other
- LCD screen like LCD1602
- 220 Ohm Resitor
- some wires
- a potentiometer

## Software

Small python script using OpenHardwareMonitor to monitor the CPU temperature and transmitting the value to the arduino over a serial connection.

### Desktop

#### findSensor.py

This script can be used to determine the name of the CPU temperatur.

In my case I use the 'CPU CCD Max' of my Ryzen 9 5950X.

#### script.py

This script sends the current temperatur every 2 seconds to the arduino.
In line 19 you can change the value you want to display.

## TODO

- [ ] Replace the LCD1602 with an OLED screen
- [ ] Build a small case to embed all hardware and 3D print it.