'''
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
'''
#we can get the a range by solving inequality condition
def check_int(n):
	return int(n)==n

def create_b(a,p):
	return (p*(p-2*a))/(2*(p-a))

k=2+2**0.5
p_value=list()
n=int(input("Enter n \n"))
p_num=list(range(1,n+1))
for p in p_num:
	count=0
	for a in range(1,int(p/k)+1):
		if check_int(create_b(a,p)):
			temp_k=p
			while temp_k<n:
				if temp_k in p_value and temp_k not in p_num:
					p_value.remove(temp_k)
				elif temp_k not in p_value and temp_k in p_num:
					p_value.append(temp_k)
					p_num.remove(temp_k)
				temp_k+=p
			break
print(len(p_value))
