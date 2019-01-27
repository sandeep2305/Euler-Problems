'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''
n=int(input())
total_sum=sum(i**i for i in range(1,n+1))
print(str(total_sum))	
