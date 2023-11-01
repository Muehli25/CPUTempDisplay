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
    
    temp_cpu = 0
    temp_gpu = 0

    for sensor in temperature_infos:
        if sensor.SensorType == 'Temperature':
            if sensor.Name == 'CPU CCD Max':
                temp_cpu = sensor.Value
            if sensor.Name == 'GPU Core':
                temp_gpu = sensor.Value

    return temp_cpu, temp_gpu

while True:
    temp_cpu, temp_gpu = get_cpu_temp()
    temperature = f"{temp_cpu},{temp_gpu}"
    ser.write(str(temperature).encode())
    time.sleep(2)
