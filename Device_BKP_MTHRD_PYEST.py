from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
from datetime import datetime
import time
import threading
import pytest


class DeviceBackup:
    def __init__(self, ip, username, password, secret='cisco', port='22', verbose=True):
        self.ip = ip
        self.username = username
        self.password = password
        self.secret = secret
        self.port = port
        self.verbose = verbose

    def backup(self):
        try:
            connection = ConnectHandler(
                device_type='cisco_ios',
                host=self.ip,
                username=self.username,
                password=self.password,
                port=self.port,
                secret=self.secret,
                verbose=self.verbose
            )

            print(f'Entering enable mode on {self.ip}...')
            connection.enable()

            print(f'\nShowing the running configuration on {self.ip}...\n')
            command_send = connection.send_command('show run')

            prompt = connection.find_prompt()
            hostname = prompt[0:-1]

            now = datetime.now()
            year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute

            filename = f'{hostname}-{year}-{month}-{day}-{hour}-{minute}-backup.txt'
            with open(filename, 'w') as backup_file:
                backup_file.write(command_send)
                print(f'Backup of {hostname} completed successfully')
                print('#' * 50)

            print('\nClosing the connection')
            connection.disconnect()

        except (NetMikoTimeoutException, SSHException, AuthenticationException) as e:
            print(f'Error occurred while connecting to {self.ip}: {e}')


@pytest.fixture(scope='module')
def netmiko_devices():
    devices = []
    with open('mydevices.txt') as f:
        mydevices1 = f.read().splitlines()

    for ip in mydevices1:
        device = DeviceBackup(ip, 'admin', 'admin', secret='cisco', port='22', verbose=True)
        devices.append(device)

    return devices


@pytest.mark.parametrize('device', netmiko_devices())
def test_backup(device):
    device.backup()


if __name__ == '__main__':
    start = time.time()
    pytest.main()
    end = time.time()
    date = datetime.now()
    print(f'Total time taken to execute this script is: {end - start}')
    print(date)
