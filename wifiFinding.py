import pywifi

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]  # Assuming you have only one wireless interface

scan_results = iface.scan_results()
for result in scan_results:
    print(f"SSID: {result.ssid}, Signal Strength: {result.signal}")
