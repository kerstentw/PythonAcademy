first_act = '''
	You find yourself standing in front of two doors.  The one on the 
right has a picture of a beautiful forest in a white picture frame.  
The one on the left has an image of a basketball.

You can choose to go through either door.

'''

second_act_r = '''
You choose the right door.  You find yourself in the forest.  It is very
nice.
'''


second_act_l = '''
You choose the left door.  You are on a basketball court.  Lebron James
walks up and punches you in the face.  Bad luck.
'''

### Game Loop

print first_act
print '\n'


print " Your choices \n \
1 - Go left \n \
2 - Go right "

try:
	choice = int(raw_input(">>>"))
	
	if choice == 1:
		print second_act_l
		
	elif choice == 2:
		print second_act_r
		
	
except:
	print "Incorrect input.  Please enter a 1 or a 2."
