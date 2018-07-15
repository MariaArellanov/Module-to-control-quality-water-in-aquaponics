import serial
import time
import requests
from pushetta import Pushetta

API_KEY = "ADD YOUR API KEY"
CHANNEL = "Water Flow"
message_service = Pushetta(API_KEY)

URL = 'https://acuaponia.herokuapp.com/'
headers = {'Content-Type':'application/json'}

arduino = serial.Serial('/dev/ttyACM0', baudrate=19200, timeout = 3.0)
#arduino.open()
data = ''

while True:
    data = arduino.readline()
    print(data)
    
    if data == '':
        continue
    elif data[0:4] == 'watr': # Modified tag for "water"
        payload = {'temp': data[4:]}
        response = requests.post(url = URL + 'water', json = payload, headers = headers)
        data = ''
    elif data[0:4] == 'ambi': # Tag for "ambient"
        payload = {'temp': data[4:]}
        response = requests.post(url = URL + 'amb', json = payload, headers = headers)
        data = ''
    elif data[0:4] == 'pump': # Tag for "pump"
        payload = {'flow': data[4:]}
        response = requests.post(url = URL + 'flow', json = payload, headers = headers)
        data = ''
    elif data == 'error':
        message_service.pushMessage(CHANNEL, '!The pump has been disconnected!')