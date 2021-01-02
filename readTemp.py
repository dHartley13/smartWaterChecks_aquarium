import os 
import glob
import time
import json
import datetime 

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder ='w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readLines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equal_pos = lines[1].find('t=')
    if equal_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        ts = datetime.dateime.utcnow().isoformat()
        
        _temp = json.dumps({'degreesCelcius':temp_c, 'degreesFarenheit': temp_f, 'ts':ts})
        return _temp

while True:
    print(read_temp)
    time.sleep(1)
    