from netmiko import ConnectHandler

cisco_devices = {
                 'device_type': 'cisco_ios',
                 'host': '123.123.1.13',
                 'username': 'admin',
                 'password': 'admin',
                 'port': '22',
                 'secret': 'cisco',
                 'verbose': True
                  }

connections = ConnectHandler(**cisco_devices)
print('Entering enable mode...')
connections.enable()


print('\nshowing the running configuration...\n')
router = connections.send_command('sho run')
print(router)

prompt = connections.find_prompt()
# print(prompt)
hostname = prompt[0:-1]
# print(hostname)
filename = f'{hostname}-backup.txt'
with open(filename, 'w') as backup:
    backup.write(router)
    print(f'Backup of {hostname} completed successfully')
    print('#' * 50)


print('\nclosing the connection')
connections.disconnect()