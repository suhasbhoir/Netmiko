from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from getpass import getpass

username = input('username: ')
password = getpass('password: ')

with open('mydevices.txt') as routers:
    router_db = routers.read().splitlines()

for ip in router_db:
    cisco_devices = {
                     'device_type': 'cisco_ios',
                     'host': ip,
                     'username': username,
                     'password': password,
                     'port': '22',
                     'secret': 'cisco',
                     'verbose': True
                      }

    try:
        connections = ConnectHandler(**cisco_devices)
    except (AuthenticationException):
        print('Authentication failure: ' + ip)
        continue
    except (NetMikoTimeoutException):
        print('Timeout to device: ' + ip)
        continue
    except (EOFError):
        print('End of file while attempting device ' + ip)
        continue
    except (SSHException):
        print('SSH Issue. Are you sure SSH is enabled? ' + ip)
        continue
    except Exception as unknown_error:
        print('Some other error: ' + str(unknown_error))

    else:
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