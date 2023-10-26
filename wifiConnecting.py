import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

profile = pywifi.Profile()
profile.ssid = 'JioFiber-eceX2'
profile.auth = pywifi.const.AUTH_ALG_OPEN
profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
profile.key = 'Techolas5g'

iface.remove_all_network_profiles()
temp_profile = iface.add_network_profile(profile)
iface.connect(temp_profile)

time.sleep(5)
if iface.status() == pywifi.const.IFACE_CONNECTED:
    print('Connected to WiFi!')
else:
    print('Connection failed.')
