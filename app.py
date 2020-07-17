import array
import getpass
import requests
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

auth = False
username = input('Ingrese su username: \n')
password = getpass.getpass('Ingrese su password: \n')
sensor_id = 0

print(password)

pload = {'username': username, 'password': password}
rq = requests.post('http://192.168.100.5:3333/users/login', data=pload)
if rq.status_code == 200:
    token = rq.json()['token']
    print('Login exitoso')
    sensor_id = int(input('Ingrese el sensor_id: \n'))
    print('\n\n')
    auth = True
else:
    print('no')

if auth:
    while True:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print('temperatura: ' + str(temperature))
            print('humedad: ' + str(humidity))
            time.sleep(1)
