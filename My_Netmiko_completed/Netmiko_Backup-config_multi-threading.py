from netmiko import ConnectHandler
from colored import fg, attr, bg
from datetime import date, datetime
from getpass import getpass
import threading
import time

start = time.time()

def router_backup(devices):
    connect = ConnectHandler(**devices)
    print('%s%s Entering to the enable mode...%s' % (fg(1), attr('bold'), attr('reset')))
    connect.enable()


    output = connect.send_command('show run')
    find_prompt = connect.find_prompt()
    router_hostname = find_prompt[0:-1]

    now = datetime.now()
    year = now.year
    month = now.year
    day = now.year
    hour = now.hour
    minute = now.minute

    filename = f'{router_hostname}_{year}_{month}_{day}_{hour}_{minute}-backup.txt'
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'\n%s%sBackup of {router_hostname} completed Successfully%s' % (fg(226), attr('bold'), attr('reset')))
        print('#' * 50)
    print('%s%sClosing the connection.....%s'% (fg(202), attr('bold'), attr('reset')))
    connect.disconnect()

with open('../mydevices.txt') as f:
    my_devices = f.read().splitlines()
username = input('%s%susername: %s' % (fg(93), attr('bold'), attr('reset')))
password = getpass('%s%sPassword: %s' % (fg(93), attr('bold'), attr('reset')))
thread111 = []
for ip in my_devices:
    cisco_devices = {
                    'device_type': 'cisco_ios',
                    'host': ip,
                    'username': username,
                    'password': password,
                    'port': '22',
                    'secret': 'cisco',
                    'verbose': True
                    }
    send_to_all = threading.Thread(target=router_backup, args=(cisco_devices,))
    thread111.append(send_to_all)

for send_to_all in thread111:
    send_to_all.start()

for send_to_all in thread111:
    send_to_all.join()

end = time.time()
date = date.today()
print('%s%sTotal execution time: %s'% (fg(93), attr('bold'), attr('reset')), (end - start))
print(date)












