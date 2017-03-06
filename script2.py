a = int(input('Enter the first number: '))
print('Your first number is:', a)
print(type(a))

b = int( input('Enter your second number: '))

if(a>b):
	print(a,'is greater than',b)
elif(a<b):
	print(a,'is less than',b)
else:
	print(a,'is equal to',b)
