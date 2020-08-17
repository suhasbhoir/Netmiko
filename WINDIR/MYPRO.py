# # Number Guessing Game implementation
# import random
# print('Guessing Number')
#
# number = random.randint(1, 21)
# chance = 0
# print('Enter the number between 1 to 20: ')
# while chance < 5:
#     guess = int(input())
#     if guess == number:
#         print('You Won!!!')
#         break
#     elif guess < number:
#         print('Your Guess was too low..Guess a number higher than', guess)
#     else:
#         print('Your Guess was too high..Guess a number lower than', guess)
#
#     chance += 1
#
# if not chance < 5:
#     print('You Lost!!! Better luck next time', number)

####################################################################
#Text-based Adventure Game- Pending from my end










#####################################################################
# Dice Rolling Simulator using Python
# import random
#
# x = "y"
# while x == "y":
#      num = random.randint(1, 6)
#      if num == 1:
#          print('|     |')
#          print('|  o  |')
#          print('|     |')
#      if num == 2:
#          print('|     |')
#          print('| oo  |')
#          print('|     |')
#      if num == 3:
#          print('|     |')
#          print('| ooo |')
#          print('|     |')
#      if num == 4:
#          print('| oo  |')
#          print('| oo  |')
#          print('|     |')
#      if num == 5:
#          print('| o  o|')
#          print('|  o  |')
#          print('| o  o|')
#      if num == 6:
#          print('| ooo |')
#          print('|     |')
#          print('| ooo |')
#
#      x = input("press 'y' to roll again and 'n' to quit: ").lower().strip()
#      print('n')



#####################################################################################
# Cisco Device backup

# from netmiko import ConnectHandler
#
# cisco_Devices = {'Device_type': 'ios',
#                  'host': 'ip',
#                  'username': 'admin',
#                  'password': 'admin1',
#                  'port': 22,
#                  'seccret': 'cisco',
#                  'verbose': True
#                  }
# connection = ConnectHandler(**cisco_Devices)
# print('Entering enable mode')
# connection.enable()
#
# cmds = '''show run
#           sho ip inter brief
#           show ip route
#           show version
#           '''
# output = connection.send_command(cmds.splitlines('\n'))
# prompt = connection.find_prompt()
# hostname = prompt[0:-1]
#
# from datetime import datetime
# now = datetime.now()
# year = now.year
# month = now.month
# day = now.day
# houre = now.hour
# minute = now.minute
#
# file = f'{hostname}_{year}_{month}_{day}_{houre}_{minute}backup.txt'
# with open(file, 'w') as backup:
#     backup.write(output)
#     print(f'Backup of {hostname} is completed successfully')
#     print('*' * 40)
#
# connection.disconnect()

########################################################################
# OS System module

import os

arp_table = os.popen('arp -a').read()
print(arp_table)
















