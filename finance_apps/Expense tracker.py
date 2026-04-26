name1 =input('what is first expense?\n')
price1 = int(input('what is first price?\n'))
name2 = input('what is second expense?\n')
price2 = int(input('what is second price?\n'))
name3 = input('what is third expense?\n')
price3 = int(input('what is third price?\n'))


Total = price1+price2+price3
print(f"{name1}: ${price1}\n{name2}: ${price2}\n{name3}: ${price3}\nTotal={Total}")
