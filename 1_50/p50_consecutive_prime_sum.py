'''The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes
'''

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True

n=int(input())
num=1
prime_num=[2]
while sum(prime_num)<n:
	if isPrime(num):
		prime_num.append(num)
	num+=2
count=0
while True:
	prime_front=sum(prime_num[count:-1])
	prime_back=sum(prime_num[:-count-1])
	if isPrime(prime_front):
		print(prime_front)
		break
	elif isPrime(prime_back):
		print(prime_back)
		break
	count+=1
