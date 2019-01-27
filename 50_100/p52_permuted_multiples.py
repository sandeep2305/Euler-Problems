'''It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.'''
num=1
while True:
	if all([True if sorted(str(num))==sorted(str(num*i)) else False for i in range(2,7)]):
		print(num)
		break
	num+=1
