# from netmiko import Netmiko
#
# connection = Netmiko(host = '123.123.1.10', port = '22', username = 'admin', password = 'admin', device_type= 'cisco_ios')

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

prompt = connections.find_prompt()
# print(prompt)
if '>' in prompt:
       connections.enable()

output = connections.send_command('show ip interface brief')
print(output)

if not connections.check_config_mode():
    connections.config_mode()
# print(connections.check_config_mode())

connections.send_command('username netmiko2 secret netmiko@123')
u1 = connections.send_command('do show run | sec user')
print(u1)

connections.exit_config_mode()
print(connections.check_config_mode())
print('\nclosing the connection')
connections.disconnect()