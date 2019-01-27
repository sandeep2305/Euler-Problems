# creating a list of amicable numbers
# Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number.
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
n=int(input())
new_num=list()
list_range=list(range(1,n+1))
total_sum=0
for i in list_range:
	temp_fact=set()
	for k in range(1,int(i/2)+1):
		if i%k==0:
			temp_fact.add(k)
	temp_sum=sum(temp_fact)
	if temp_sum>i and temp_sum<=n:
		temp_fact2=set()
		for l in range(1,int(temp_sum/2)+1):
			if temp_sum%l==0:
				temp_fact2.add(l)
		temp_sum2=sum(temp_fact2)
		if temp_sum2==i:
			list_range.remove(temp_sum)
			new_num.append([i,temp_sum])
			total_sum+=temp_sum+i
print(new_num)
print(total_sum)
