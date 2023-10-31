import serial
import time
import wmi

ser = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino's COM port

OHM_hwtypes = ['Mainboard', 'SuperIO', 'CPU', 'RAM', 'GpuNvidia', 'GpuAti', 'TBalancer', 'Heatmaster', 'HDD']
OHM_sensortypes = [
    'Voltage', 'Clock', 'Temperature', 'Load', 'Fan', 'Flow', 'Control', 'Level', 'Factor', 'Power', 'Data', 'SmallData'
]


def get_cpu_temp():
    w = wmi.WMI(namespace="root/OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    
    for sensor in temperature_infos:
        if sensor.SensorType == 'Temperature':
            if sensor.Name == 'CPU CCD Max':
                return sensor.Value

    return -1

while True:
    temperature = get_cpu_temp()
    ser.write(str(temperature).encode())
    time.sleep(2)
