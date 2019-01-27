'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''
import numpy as np
file_read=open("p_triangle.txt","r")
tri_value=[]
line=file_read.readline()
while line:
	tri_value.append(list(map(int,line.split())))
	line=file_read.readline()
tri_zero=[i+[0]*(len(tri_value)-len(i)) for i in tri_value]
tri_matrix=np.matrix(tri_zero)
m,n=tri_matrix.shape
print(m,n)
for j in range(m-1,0,-1):
	for k in range(0,n-1):
			tri_matrix[j-1,k]+=max([tri_matrix[j,k],tri_matrix[j,k+1]])
print(tri_matrix[0,0])
