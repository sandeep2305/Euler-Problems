'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?'''

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True
 
def primeList(n):
	if n<2: 
		return[]
	else:
		prime_list=[2]
		count=1
		while count<=n:
			if isPrime(count):
				prime_list.append(count)
			count+=2
		return prime_list

#circular rotation by 1
		
def rotate_string(str_input):
	return str_input[-1]+str_input[:-1]
   
n=int(input())
prime_num_list=primeList(n)
circular_prime=list()
for i in prime_num_list:
	num_str=str(i)
	if len(num_str)<2:
		circular_prime.append(i)
	else:
		for k in range(1,len(num_str)):
			num_str=rotate_string(num_str)
			if not isPrime(int(num_str)):
				break
		else:
			circular_prime.append(i)
print(len(circular_prime))
	
