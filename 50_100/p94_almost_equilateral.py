'''
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
'''
def check_int(n):
	return int(n)==n
	
n=int(input("Enter n \n"))
num=2
while 3*num+1<=n:
	if check_int(0.25*(num+1)*(3*num*num-2*num-1)**0.5) or check_int(0.25*num*(3*num*num+8*num+4)**0.5) :
		print(3*num+1)
	num+=1
