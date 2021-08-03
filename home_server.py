import requests
import json
import time

AWS_IP = "http://18.234.97.9" #CHANGE THIS WHEN YOU START YOUR EC2 INSTANCE

SENSOR_IP = "http://192.168.11.71"  #CHANGE THIS WHEN YOU START YOUR NODE MCU

while (True):
    time.sleep(1)
    print("Asking F2 for values")
    value = requests.get("{}:5001/get_values".format(AWS_IP), timeout=5)
    value = json.loads(value.content)

    try :

        if value['led'] == 'on':
            print("TELLING NODE MCU TO SWITCH ON LED")
            requests.get("{}/LED=ON".format(SENSOR_IP), timeout=5)
        elif value['led'] == 'off':
            print("TELLING NODE MCU TO SWITCH OFF LED")
            requests.get("{}/LED=OFF".format(SENSOR_IP), timeout=5)

        if value['door'] == 'open':
            print("tell to open door")
            requests.get("{}/DOOR=OPEN".format(SENSOR_IP), timeout=5)
        elif value['door'] == 'close':
            print("telling to close door")
            requests.get("{}/DOOR=CLOSE".format(SENSOR_IP), timeout=5)



        if value['dht'] == 'on':
            print('telling mcu to on dht')
            requests.get("{}/DHT=ON".format(SENSOR_IP), timeout=5)
        elif value['dht'] == 'off':
            print('telling node mcu to off dht')
            requests.get("{}/DHT=OFF".format(SENSOR_IP), timeout=5)

        if value['buzzer'] == 'on':
            print('telling node mcu to on buzzer')
            requests.get("{}/BUZZER=ON".format(SENSOR_IP), timeout=5)
        elif value['buzzer'] == 'off':
            print('telling node mcu to off buzzer')
            requests.get("{}/BUZZER=OFF".format(SENSOR_IP), timeout=5)

        if value['gas_detector'] == 'on':
            print('telling node mcu to on gas detector')
            requests.get("{}/GAS=ON".format(SENSOR_IP), timeout=5)
        elif value['gas_detector'] == 'off':
            print('telling node mcu to off gas detector')
            requests.get("{}/GAS=OFF".format(SENSOR_IP), timeout=5)

    
    except:
        pass