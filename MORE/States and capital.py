from colored import fg,attr

states_and_capital = {'Andhra Pradesh': {'capital': 'Hyderabad','Founded on': '1 Nov. 1956'},
					  'Arunachal Pradesh': {'capital': 'Itanagar','Founded on': '20 Feb. 1987'},
				      'Assam': {'capital': 'Dispur','Founded on': '26 Jan. 1950'},
	                  'Bihar': {'capital': 'Patna','Founded on': '26 Jan. 1950'},
	                  'Chhattisgarh': {'capital': 'Raipur','Founded on': '1 Nov. 2000'},
	                  'Goa': {'capital': 'Panaji','Founded on': '30 May. 1987'},
	                  'Gujarat': {'capital': 'Gandhinagar','Founded on': '1 May. 1960'},
	                  'Haryana': {'capital': 'Chandigarh','Founded on': '1 Nov. 1966'},
				      'Himachal Pradesh':	{'capital': 'Shimla','Founded on': '25 Jan. 1971'},
	 			      'Jharkhand':	{'capital': 'Ranchi','Founded on': '15 Nov. 2000'},
	                  'Karnataka':	{'capital': 'Bengaluru (formerly Bangalore)','Founded on': '1 Nov. 1956'},
	                  'Kerala':	{'capital': 'Thiruvananthapuram','Founded on': '1 Nov. 1956'},
					  'Madhya Pradesh':	{'capital': 'Bhopal','Founded on': '1 Nov. 1956'},
				 	  'Maharashtra':	{'capital': 'Mumbai','Founded on': '1 May. 1960'},
					  'Manipur':	{'capital': 'Imphal','Founded on': '21 Jan. 1972'},
					  'Meghalaya':	{'capital': 'Shillong','Founded on': '21 Jan. 1972'},
					  'Mizoram':	{'capital': 'Aizawl','Founded on': '20 Feb. 1987'},
					  'Nagaland':	{'capital': 'Kohima','Founded on': '1 Dec. 1963'},
					  'Odisha':	{'capital': 'Bhubaneswar','Founded on': '26 Jan. 1950'},
					  'Punjab':	{'capital': 'Chandigarh','Founded on': '1 Nov. 1956'},
					  'Rajasthan':	{'capital': 'Jaipur','Founded on': '1 Nov. 1956'},
					  'Sikkim': 	{'capital': 'Gangtok','Founded on': '16 May. 1975'},
					  'Tamil Nadu':	{'capital': 'Chennai','Founded on': '26 Jan. 1950'},
					  'Telangana':	{'capital': 'Hyderabad','Founded on': '2 Jun. 2014'},
					  'Tripura':	{'capital': 'Agartala','Founded on': '21 Jan. 1972'},
					  'Uttar Pradesh':	{'capital': 'Lucknow','Founded on': '26 Jan. 1950'},
					  'Uttarakhand':	{'capital': 'Dehradun (Winter) Gairsain (Summer)','Founded on': '9 Nov. 2000'},
					  'West Bengal':	{'capital': 'Kolkata','Founded on': '1 Nov. 1956'}
					  }

print('\nStates and their capital, Choose the state to know the capital')
print('For ex: <enter 14 no to know the capital of Maharashtra>\n')

print('1. Andhra Pradesh\n'
	  '2. Arunachal Pradesh\n'
	  '3. Assam\n'
	  '4. Bihar\n'
	  '5. Chhattisgarh\n'
	  '6. Goa\n'
	  '7. Gujarat\n'
	  '8. Haryana\n'
	  '9. Himachal Pradesh\n'
	  '10. Jharkhand\n'
	  '11. Karnataka\n'
	  '12. Kerala\n'
	  '13. Madhya Pradesh\n'
	  '14. Maharashtra\n'
	  '15. Manipur\n'
	  '16. Meghalaya\n'
	  '17. Mizoram\n'
	  '18. Nagaland\n'
	  '19. Odisha\n'
	  '20. Punjab\n'
	  '21. Rajasthan\n'
	  '22. Sikkim\n'
	  '23. Tamil Nadu\n'
	  '24. Telangana\n'
	  '25. Tripura\n'
	  '26. Uttar Pradesh\n'
	  '27. Uttarakhand\n'
	  '28. West Bengal\n')
print('Above are the lists of all states in BHARAT')
all_states = []
for keys in states_and_capital:
	all_states.append(keys)
# print(all_states)
# print('\n',all_states[0])
while True:
	userinp = int(input('enter the Number of state to know their \'capital\': '))
	if userinp == 1:
		print('\n%s%s You choose %s' %(fg(154),attr('bold'), all_states[0]))
		print('#' * 50)
		print('And Capital of ', all_states[0], 'is ', states_and_capital['Andhra Pradesh']['capital'])
		print('And it is founded on ', states_and_capital['Andhra Pradesh']['Founded on'])
		print('_' * 50)
	elif userinp == 2:
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[1]))
		print('#' * 50)
		print('And Capital of ', all_states[1], 'is ', states_and_capital['Arunachal Pradesh']['capital'])
		print('And it is founded on ', states_and_capital['Arunachal Pradesh']['Founded on'])
		print('_' * 50)
	elif userinp == 3:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[2]))
		print('And Capital of ', all_states[2], 'is ', states_and_capital['Assam']['capital'])
		print('And it is founded on ', states_and_capital['Assam']['Founded on'])
		print('_' * 50)
	elif userinp == 4:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[3]))
		print('And Capital of ', all_states[3], 'is ', states_and_capital['Bihar']['capital'])
		print('And it is founded on ', states_and_capital['Bihar']['Founded on'])
		print('_' * 50)
	elif userinp == 5:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[4]))
		print('And Capital of ', all_states[4], 'is ', states_and_capital['Chhattisgarh']['capital'])
		print('And it is founded on ', states_and_capital['Chhattisgarh']['Founded on'])
		print('_' * 50)
	elif userinp == 6:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[5]))
		print('And Capital of ', all_states[5], 'is ', states_and_capital['Goa']['capital'])
		print('And it is founded on ', states_and_capital['Goa']['Founded on'])
		print('_' * 50)
	elif userinp == 7:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[6]))
		print('And Capital of ', all_states[6], 'is ', states_and_capital['Gujarat']['capital'])
		print('And it is founded on ', states_and_capital['Gujarat']['Founded on'])
		print('_' * 50)
	elif userinp == 8:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[7]))
		print('And Capital of ', all_states[7], 'is ', states_and_capital['Haryana']['capital'])
		print('And it is founded on ', states_and_capital['Haryana']['Founded on'])
		print('_' * 50)
	elif userinp == 9:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[8]))
		print('And Capital of ', all_states[8], 'is ', states_and_capital['Himachal Pradesh']['capital'])
		print('And it is founded on ', states_and_capital['Himachal Pradesh']['Founded on'])
		print('_' * 50)
	elif userinp == 10:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[9]))
		print('And Capital of ', all_states[9], 'is ', states_and_capital['Jharkhand']['capital'])
		print('And it is founded on ', states_and_capital['Jharkhand']['Founded on'])
		print('_' * 50)
	elif userinp == 11:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[10]))
		print('And Capital of ', all_states[10], 'is ', states_and_capital['Karnataka']['capital'])
		print('And it is founded on ', states_and_capital['Karnataka']['Founded on'])
		print('_' * 50)
	elif userinp == 12:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[11]))
		print('And Capital of ', all_states[11], 'is ', states_and_capital['Kerala']['capital'])
		print('And it is founded on ', states_and_capital['Kerala']['Founded on'])
		print('_' * 50)
	elif userinp == 13:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[12]))
		print('And Capital of ', all_states[12], 'is ', states_and_capital['Madhya Pradesh']['capital'])
		print('And it is founded on ', states_and_capital['Madhya Pradesh']['Founded on'])
		print('_' * 50)
	elif userinp == 14:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[13]))
		print('And Capital of ', all_states[13], 'is ', states_and_capital['Maharashtra']['capital'])
		print('And it is founded on ', states_and_capital['Maharashtra']['Founded on'])
		print('_' * 50)
	elif userinp == 15:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[14]))
		print('And Capital of ', all_states[14], 'is ', states_and_capital['Manipur']['capital'])
		print('And it is founded on ', states_and_capital['Manipur']['Founded on'])
		print('_' * 50)
	elif userinp == 16:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[15]))
		print('And Capital of ', all_states[15], 'is ', states_and_capital['Meghalaya']['capital'])
		print('And it is founded on ', states_and_capital['Meghalaya']['Founded on'])
		print('_' * 50)
	elif userinp == 17:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[16]))
		print('And Capital of ', all_states[16], 'is ', states_and_capital['Mizoram']['capital'])
		print('And it is founded on ', states_and_capital['Mizoram']['Founded on'])
		print('_' * 50)
	elif userinp == 18:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[17]))
		print('And Capital of ', all_states[17], 'is ', states_and_capital['Nagaland']['capital'])
		print('And it is founded on ', states_and_capital['Nagaland']['Founded on'])
		print('_' * 50)
	elif userinp == 19:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[18]))
		print('And Capital of ', all_states[18], 'is ', states_and_capital['Odisha']['capital'])
		print('And it is founded on ', states_and_capital['Odisha']['Founded on'])
		print('_' * 50)
	elif userinp == 20:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[19]))
		print('And Capital of ', all_states[19], 'is ', states_and_capital['Punjab']['capital'])
		print('And it is founded on ', states_and_capital['Punjab']['Founded on'])
		print('_' * 50)
	elif userinp == 21:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[20]))
		print('And Capital of ', all_states[20], 'is ', states_and_capital['Rajasthan']['capital'])
		print('And it is founded on ', states_and_capital['Rajasthan']['Founded on'])
		print('_' * 50)
	elif userinp == 22:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[21]))
		print('And Capital of ', all_states[21], 'is ', states_and_capital['Sikkim']['capital'])
		print('And it is founded on ', states_and_capital['Sikkim']['Founded on'])
		print('_' * 50)
	elif userinp == 23:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[22]))
		print('And Capital of ', all_states[22], 'is ', states_and_capital['Tamil Nadu']['capital'])
		print('And it is founded on ', states_and_capital['Tamil Nadu']['Founded on'])
		print('_' * 50)
	elif userinp == 24:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[23]))
		print('And Capital of ', all_states[23], 'is ', states_and_capital['Telangana']['capital'])
		print('And it is founded on ', states_and_capital['Telangana']['Founded on'])
		print('_' * 50)
	elif userinp == 25:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[24]))
		print('And Capital of ', all_states[24], 'is ', states_and_capital['Tripura']['capital'])
		print('And it is founded on ', states_and_capital['Tripura']['Founded on'])
		print('_' * 50)
	elif userinp == 26:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[25]))
		print('And Capital of ', all_states[25], 'is ', states_and_capital['Uttar Pradesh']['capital'])
		print('And it is founded on ', states_and_capital['Uttar Pradesh']['Founded on'])
		print('_' * 50)
	elif userinp == 27:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[26]))
		print('And Capital of ', all_states[26], 'is ', states_and_capital['Uttarakhand']['capital'])
		print('And it is founded on ', states_and_capital['Andhra Pradesh']['Founded on'])
		print('_' * 50)
	elif userinp == 28:
		print('#' * 50)
		print('%s%s You choose %s' %(fg(154),attr('bold'), all_states[27]))
		print('And Capital of ', all_states[27], 'is ', states_and_capital['West Bengal']['capital'])
		print('And it is founded on ', states_and_capital['West Bengal']['Founded on'])
		print('_' * 50)
	stop = str(input('Press \'Y\' to continue or \'N\' to exit: ')).lower().strip()
	if stop == 'y':
		continue
	elif stop == 'n':
		break
	else:
		print('Invalid input detected')
