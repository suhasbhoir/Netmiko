from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime
from getpass import getpass
import time
import threading  # Now enabling ihe multi-threading

"""import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")"""


start = time.time()

def backup(devices):
    connections = ConnectHandler(**devices)
    print('Entering enable mode...')
    connections.enable()

    print('\nshowing the running configuration...\n')


    with open('cmd.txt') as command:
        for c in command:
            output = connections.send_command(c)
            print(output)

            prompt = connections.find_prompt()
            # print(prompt)
            hostname = prompt[0:-1]
            # print(hostname)

            now = datetime.now()
            year = now.year
            month = now.month
            day = now.day
            hour = now.hour
            minute = now.minute

            filename = f'{hostname}-{year}-{month}-{day}-{hour}-{minute}-backup.txt'
            with open(filename, 'w') as backup:
                backup.write(output)
                print(f'Backup of {hostname} completed successfully')
                print('#' * 50)

            print('\nclosing the connection')
            connections.disconnect()


with open('mydevices.txt') as f:
    mydevices1 = f.read().splitlines()


threads1 = list()# Created a list here before for loop whaer th value will be added
username = input('username: ')
password = getpass('password: ')

for ip in mydevices1:
    cisco_devices = {
                     'device_type': 'cisco_ios',
                     'host': ip,
                     'username': username,
                     'password': password,
                     'port': '22',
                     'secret': 'cisco',
                     'verbose': True
                      }


    th = threading.Thread(target=backup, args=(cisco_devices, ) )#created thread here
    threads1.append(th)


for th in threads1:
    th.start()
for th in threads1:
    th.join()
end = time.time()
print(f'Total time took to execution this script is: {end - start}')
