from netmiko import ConnectHandler

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
print('Entering enable mode...')
connections.enable()

# commands = ['interface loop 1', 'ip address 1.1.1.1 255.255.255.255',
#             'interface loop 10', 'ip address 10.10.10.10 255.255.255.255', 'exit',
#             'username netmiko3 secret netmiko@123']
# commands1 = 'ip ssh ver 2;access-list 1 permit any;'

commands2 = ''' ip ssh ver 2
access-list 2 permit any
ip access-list ext 101
permit ip any any
'''

# output = connections.send_config_set(commands)
# output = connections.send_config_set(commands1.split(';'))
output = connections.send_config_set(commands2.split('\n'))
print(output)

print(connections.find_prompt())

wr = connections.send_command('write memory')
print(wr)


print('\nclosing the connection')
connections.disconnect()