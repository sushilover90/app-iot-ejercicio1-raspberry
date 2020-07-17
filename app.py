from datetime import datetime
from pprint import pprint
import json
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
    print('Login exitoso\n')
    sensor_id = int(input('Ingrese el sensor_id: \n'))
    cantidad_lecturas_mongo = int(input('Ingrese el numero de lecturas a registrar en mongo: \n'))
    clear()
    auth = True
else:
    print('no')

if auth:
    while True:

        if(len(lecturas)) == cantidad_lecturas_mongo:
            now = datetime.now()
            _pload = {"sensor_id":sensor_id,'fecha_registro':now.strftime('%Y/%m/%d'),'hora_registro':now.strftime('%H:%M:%S'),'lecturas':lecturas}
            _rq = requests.post('http://192.168.100.5:3333/sensores/lecturas/register',json=_pload)
            if _rq.status_code == 200:
                now = datetime.now()
                clear()
                print('Hora del registro: ' + now.strftime('%Y/%m/%d') + ' ' + now.strftime('%H:%M:%S'))
                print(_rq.json())
                lecturas = []
            else:
                now = datetime.now()
                print('Hubo un error en el registro. Hora: ' + now.strftime('%Y/%m/%d') + '\n')

        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
        if humidity is not None and temperature is not None:
            now = datetime.now()
            lecturas.append({'fecha_registro':now.strftime('%Y/%m/%d'),'hora_registro':now.strftime('%H:%M:%S'),'temperatura':temperature,'humedad':humidity})
            time.sleep(1)

