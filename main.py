import psutil
import platform
import socket
import os
import time
from datetime import datetime

def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM Size (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Disk Size (GB)": round(psutil.disk_usage('/').total / (1024 ** 3), 2),
        "Uptime": str(datetime.now() - datetime.fromtimestamp(psutil.boot_time()))
    }
    return system_info
def getbattery_info():
    battery = psutil.sensors_battery()
    if battery:
        battery_info = {
            "Battery Percentage": battery.percent,
            "Charging": battery.power_plugged,
            "Time Left (seconds)": battery.secsleft
        }
    else:
        battery_info = {
            "Battery Percentage": None,
            "Charging": None,
            "Time Left (seconds)": None
        }
    return battery_info

def get_network_info():
    network_info = {}
    for interface, addrs in psutil.net_if_addrs().items():
        network_info[interface] = []
        for addr in addrs:
            if addr.family == socket.AF_INET:
                network_info[interface].append({
                    "IP Address": addr.address,
                    "Netmask": addr.netmask,
                    "Broadcast IP": addr.broadcast
                })
            elif addr.family == socket.AF_INET6:
                network_info[interface].append({
                    "IPv6 Address": addr.address,
                    "Netmask": addr.netmask,
                    "Broadcast IP": addr.broadcast
                })
            elif addr.family == psutil.AF_LINK:
                network_info[interface].append({
                    "MAC Address": addr.address
                })
    return network_info

def get_health_status():
    health_status = {
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "RAM Usage (%)": psutil.virtual_memory().percent,
        "Disk Usage (%)": psutil.disk_usage('/').percent,
        "Battery Info": getbattery_info(),
        "Network Info": get_network_info()
    }
    return health_status

print("System Information:")
system_info = get_system_info()
for key, value in system_info.items():
    print(f"{key}: {value}")

print("\nHealth Status:")
health_status = get_health_status()
for category, metrics in health_status.items():
    print(f"{category}:")
    if isinstance(metrics, dict):
        for key, value in metrics.items():
            print(f"  {key}: {value}")
    else:
        print(f"  {metrics}")

    print("\nNetwork Information:")
network_info = get_network_info()
for interface, addrs in network_info.items():
    print(f"{interface}:")
    for addr in addrs:
        for key, value in addr.items():
            print(f"  {key}: {value}")

print("\nBattery Information:")
battery_info = getbattery_info()
for key, value in battery_info.items():
    print(f"  {key}: {value}")

print("\nSystem Health Monitoring:")
while True:
    health_status = get_health_status()
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Health Status:")
    for category, metrics in health_status.items():
        print(f"{category}:")
        if isinstance(metrics, dict):
            for key, value in metrics.items():
                print(f"  {key}: {value}")
        else:
            print(f"  {metrics}")
    time.sleep(10)  # Update every 10 seconds
    print("\n Thank you for using D.TALA'S System Health Monitoring Tool. The system health status will be updated every 10 seconds. ")
    print("\nPress Ctrl+C to stop monitoring.")