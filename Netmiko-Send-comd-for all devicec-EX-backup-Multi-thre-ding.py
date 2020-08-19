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

def backup(devices):
    connections = ConnectHandler(**devices)
    print('Entering enable mode...')
    connections.enable()

    print('\nshowing the running configuration...\n')
    cmds = '''sho run
              sho ip route
              show route-map
              show ip protocols
              '''
    output = connections.send_command(cmds.splitlines('\n'))
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
# backup(cisco_devices)
    #creating thread here
    th = threading.Thread(target=backup, args=(cisco_devices, ) )
    threads1.append(th)

for th in threads1:
    th.start()

for th in threads1:
    th.join()



end = time.time()
print(f'Total time took to execution this script is: {end - start}')