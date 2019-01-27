#Smallest number which is evenly divisible by num 1 to n 
# evenly divisible means without reminder
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

n=int(input())
num=1
for i in range(2,n+1):
	if num%i!=0:
		for k in range(2,i):
			if i%k==0:
				num=num*k
				break
		else:
			num=num*i
print(num)
