'''the number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''
from itertools import permutations
#given number
num_str='1234567890'
divider=[2,3,5,7,11,13,17]
propert_num=list()
all_num=list("".join(i) for i in list(permutations(num_str)))
for k in all_num:
	if all([True if int(k[l+1:l+4])%divider[l]==0 else False for l in range(0,7) ]):
		propert_num.append(int(k))
print(propert_num)
print(sum(propert_num))
