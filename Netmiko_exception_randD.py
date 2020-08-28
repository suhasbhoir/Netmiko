from netmiko import ConnectHandler
with open('mydevices.txt') as f:
    mydevices1 = f.read().splitlines()

devices_list = list()

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
    devices_list.append(cisco_devices)

    connection = ConnectHandler()

