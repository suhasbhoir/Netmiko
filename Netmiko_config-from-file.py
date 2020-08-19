from netmiko import ConnectHandler
# import logging
# logging.basicConfig(filename='test.log', level=logging.DEBUG)
# logger = logging.getLogger("netmiko")

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

print('Sending configuration from file...')
c1 = connections.send_config_from_file('config.txt')
print(c1)

print('\nshowing the summary of OSPF configuration...\n')
router = connections.send_command('sho run')
print(router)



print('\nclosing the connection')
connections.disconnect()