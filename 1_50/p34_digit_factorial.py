'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.'''
import math
n=int(input())
list_num=list(range(3,n+1))
sum_num=0
for i in list_num:
	list_a=list(str(i))
	temp_sum=0
	for j in list_a:
		temp_sum+=int(math.factorial(int(j)))
	if temp_sum==i:
		sum_num+=i
		print(i)
print(sum_num)
