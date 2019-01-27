# Differce in square of n natual sum to square of sum of the num
'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
n=int(input())
sum_of_sq=0
sum_of_num=0
for i in range(n+1):
	sum_of_sq+=i**2
	sum_of_num+=i
print(sum_of_num**2-sum_of_sq)
