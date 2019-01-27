#longest collatz sequence under 1000000
# for even n/2 and for odd 3n+1
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import time
initial_time=time.time()
Cnum=1000000-1
num_with_max=0
while (Cnum)>1:
	z=Cnum
	chain_of=[z]
	while z>1:
		if z%2==0:
			z=int(z/2)
			chain_of.append(z)
		else:
			z=3*z+1
			chain_of.append(z)
	temp_max=len(chain_of)
	if temp_max>num_with_max:
		num_with_max=temp_max
		max_len_num=chain_of
		longest=Cnum
	Cnum+=-2
print(num_with_max)
print(max_len_num)
print(longest)
final_time=time.time()
print(final_time-initial_time)
