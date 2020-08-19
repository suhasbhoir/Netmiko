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

# print(devices_list)
# exit(0)
for device in devices_list:
    connections = ConnectHandler(**device)


    print('Entering enable mode...')
    connections.enable()

    file = input(f'Enter a configuration file for {device["host"]}: ')

    print(f'running command from file: {file} on device {device["host"]}')

    c1 = connections.send_config_from_file(file)
    print(c1)

    print(f'closing connection to {cisco_devices["host"]}')
    connections.disconnect()

    print('#' * 50)