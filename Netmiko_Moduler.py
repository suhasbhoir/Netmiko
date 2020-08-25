from netmiko import ConnectHandler
from colored import fg, attr, bg
from datetime import datetime
import threading
import time


def cisco(routers):
    connect = ConnectHandler(**routers)
    print('%s%s Entering to the enable mode...%s' % (fg(1), attr('bold'), attr('reset')))
    connect.enable()

    with open('cmd.txt', 'r') as c:
        cli = c.read().splitlines()
    print('%s%sEntering the show commands from repository%s' % (fg(2), attr('bold'), attr('reset')), cli)
    send_cmd = input('Do you want to send above commands to the devices. Hit < Y for yes | Nfor No >').lower().strip()

    if send_cmd == 'y':
        print('%s%sSending commands to the devices%s' % (fg(196), attr('bold'), attr('reset')))
        output = connect.send_command(cli)
        find_prompt = connect.find_prompt()
        router_hostname = find_prompt[0:-1]

        now = datetime.now()
        year = now.year
        month = now.year
        day = now.year
        hour = now.hour
        minute = now.minute

        filename = f'{router_hostname}_{year}_{month}_{day}_{hour}_{minute}_backup.txt'
        with open(filename, 'w') as backup:
            backup.write(output)
            print(f'%s%sBackup of {router_hostname} completed Successfully%s' % (fg(226), attr('bold'), attr('reset')))
            print('%s%s#%s' * 50 %(fg(200), attr('bold'), attr('reset')))
    elif send_cmd == 'n':
        print('You terminate the operation... Closing the connections to devices')
        connect.disconnect()
        print('%s%s*%s' * 50 % (fg(200), attr('bold'), attr('reset')))
    else:
        print('%s%sInvalid input detected !!!%s' % (fg(200), attr('bold'), attr('reset')))

with open('mydevices.txt') as device_list:
    my_devices = device_list.read().splitlines()
thread = []













