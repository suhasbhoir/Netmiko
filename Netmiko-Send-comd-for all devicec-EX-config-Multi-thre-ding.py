from netmiko import ConnectHandler
from datetime import datetime
import time
import threading  # Now enabling ihe multi-threading
'''
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
'''

start = time.time()

def configsend(devices):
    connections = ConnectHandler(**devices)
    print('Entering enable mode...')
    connections.enable()

    print('\nApplying configuration to devices from file...\n')
    router = connections.send_config_from_file('config.txt')
    print(router)


    print('\nclosing the connection')
    connections.disconnect()


with open('mydevices.txt') as f:
    mydevices1 = f.read().splitlines()

# Creating a list here before for loop
threads1 = list()
for ip in mydevices1:
    cisco_devices = {
                     'device_type': 'cisco_ios',
                     'host': ip,
                     'username': 'admin',
                     'password': 'admin',
                     'port': '22',
                     'secret': 'cisco',
                     'verbose': True
                      }

    #creating thread here
    th = threading.Thread(target=configsend, args=(cisco_devices, ) )
    threads1.append(th)

for th in threads1:
    th.start()

for th in threads1:
    th.join()



end = time.time()
print(f'Total time took to execution this script is: {end - start}')