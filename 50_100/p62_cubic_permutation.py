'''The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''
from itertools import permutations

def is_perfect_cube(x):
    return int(round(x ** (1. / 3))) ** 3 == x

def permuta_num(array):
	return list(set(map(int,["".join(i) for i in list(permutations(array))])))

n=int(input())
num=9
while True:
	count=0
	for i in permuta_num(str(num**3)):
		if is_perfect_cube(i):
			count+=1
	print(num)
	if count==n:
		break
		print(count)
	num+=1
	
