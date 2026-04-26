Grade = int(input('Enter your score: '))
if Grade >= 101 :
    print('Wrong input')
elif Grade >= 85 :
	print('A')
	print('Excellence')
elif Grade >= 70 :
	print('B')
	print('Very good')
elif Grade >= 60 :
	print('C')
	print('Good')
elif Grade >= 50 :
	print('D')
	print('Fair')
else:
	print('F')
	print('You can do better next time')
