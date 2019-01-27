'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
# if we take a and b as side so c must be sqrt(a2+b2)
# p will be always greater than 1
# b=p-(sqrt(a^2+b^2))
# now with calulation of a+b+c=p we will get b in terms of a and p

def check_int(n):
	return int(n)==n

max_count=0
p_value=0
k=2+2**0.5
sides=list()
n=int(input())
for p in range(10,n+1):
	count=0
	temp_sides=list()
	for a in range(1,int(p/k)+1):
		b=(p*(p-2*a))/(2*(p-a))
		if check_int(b) and b>a:
			count+=1
			temp_sides.append([a,b])
	if count==1:
		max_count=count
		print(p,count)
		p_value=p
		sides=temp_sides
print([max_count,p_value,sides])
