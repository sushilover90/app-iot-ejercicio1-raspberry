from datetime import datetime
from pprint import pprint
import os
import getpass
import requests
import Adafruit_DHT
import time

clear = lambda: os.system('clear')

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

auth = False
registering = False
token = ""
clear()
username = input('Ingrese su username: \n')
password = getpass.getpass('Ingrese su password: \n')
sensor_id = 0
pload = {'username':username,'password':password}
rq = requests.post('http://192.168.100.5:3333/users/login',data = pload)
lecturas = []

if rq.status_code == 200:
    token = rq.json()['token']
    print('Login exitoso')
    sensor_id = int(input('Ingrese el sensor_id: \n'))
    clear()
    auth = True
else:
    print('no')

if auth:
    while True:

        if(len(lecturas)) == 2:

                now = datetime.now()
                _pload = {"sensor_id":sensor_id,'fecha_registro':now.strftime('%Y/%m/%d'),'hora_registro':now.strftime('%H:%M:%S'),'lecturas':lecturas}
                _rq = requests.post('http://192.168.100.5:3333/sensores/lecturas/register',data=_pload)
                clear()
                pprint(lecturas)
                print('\n')
                pprint(_rq.json())
                lecturas = []
                #print('registrao')

        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
        if humidity is not None and temperature is not None:
            #print('temperatura: ' + str(temperature))
            #print('humedad: ' + str(humidity))
            #print(now.strftime('%Y/%m/%d'))
            #print(now.strftime('%H:%M:%S'))
            now = datetime.now()
            lecturas.append({'fecha_registro':now.strftime('%Y/%m/%d'),'hora_registro':now.strftime('%H:%M:%S'),'temperatura':temperature,'humedad':humidity})
            #pprint(lecturas)
            #print(len(lecturas))

            time.sleep(1)


