Balance = int(input('enter your balance\n'))
name1 = input('Enter first expense:\n')
price1 = int(input(('enter first price:\n')))
name2 = input('Enter second expense:\n')
price2 = int(input(('enter second price:\n')))
name3 = input(('enter third expense:\n'))
price3 = int(input('Enter third price:\n'))
Total = price1+price2+price3
if Total >= Balance :
     print('You have exceeded your balance')
elif Total < Balance :
      amount_left = Balance - Total
      print(f"you still have:  ${amount_left}")
