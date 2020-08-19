from netmiko import ConnectHandler

import logging
logging.basicConfig(filename='int1.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")


cisco_devices = {
       'device_type': 'cisco_ios',
       'host': '123.123.1.10',
       'username': 'admin',
       'password': 'admin',
       'port': '22',
       'secret': 'cisco',
       'verbose': True
       }
connections = ConnectHandler(**cisco_devices)
prompter = connections.find_prompt()
if '>' in prompter:
    connections.enable()

interface = input('Please enter the interface you want to enable: ')
cmdout = connections.send_command('show ip interface brief' + interface)

if 'Invalid input detected' in cmdout:
    print('You entered invalid interface')
else:
    first_line = cmdout.splitlines() [0]
    print(first_line)
    if not 'ip' in first_line:
        print('The interface is down...Enabling the interface..')
        commands = ['interface' + interface, 'no shut', 'exit']
        transfer_cmd = connections.send_config_set(commands)
        print(cmdout)
        print('#' * 50)
        print('The interface has been enabled')
    else:
        print('interface ' + interface + ' is already enabled')