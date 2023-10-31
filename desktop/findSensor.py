import wmi

def get_ohm_data():
    sensor_data = {}

    w = wmi.WMI(namespace="root/OpenHardwareMonitor")
    temperature_infos = w.Sensor()

    for sensor in temperature_infos:
        if sensor.SensorType == 'Temperature':
            print(f"{sensor.Name}: {sensor.Value}°C")

get_ohm_data()