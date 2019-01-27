# number to find summation of all primes below number
'''
e sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import time
hi = int(input())
a=time.time()
# create a set excluding even numbers
numbers = set(range(3, hi + 1, 2)) 

for number in range(3, int(hi ** 0.5) + 1):
	if number not in numbers:
        #number must have been removed because it has a prime factor 
		continue
	num = number
	while num < hi:
		num += number
		if num in numbers:
            		numbers.remove(num)
b=time.time()
print (2 + sum(numbers))
print(b-a)
