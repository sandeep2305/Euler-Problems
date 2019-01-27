'''creating a matrix and searching for largest product of n digits from left to right, up to down and both diagonal, which ever is max we have to calculate'''
import numpy as np
from functools import reduce

# calculate left to right of sub matix product
def left_right(temp_mat):
	return reduce(lambda y, z : y* z , temp_mat[0,:])

#calculate up to down of sub matrix product
def up_down(temp_mat):
	return reduce(lambda y ,z : y* z , temp_mat[:,0])

# calculte diagonal of the matrix product
def dia_up(temp_mat):
	return reduce(lambda y ,z : y* z , np.diagonal(temp_mat))

#calculate other diagonal
def dia_down(temp_mat):
	return reduce(lambda y ,z : y* z , np.diagonal(np.fliplr(temp_mat)))

file_read=open("matrix.txt","r")
mat_cre=[]
k=int(input()) #no of digits we have to get product of raw_input=input in python3
line=file_read.readline()
while line:
	mat_cre.append(list(map(int,line.split())))
	line=file_read.readline()
file_read.close()
max_product=0
mat_cre_np=np.array(mat_cre)
m,n=mat_cre_np.shape
for i in range(m):
	for j in range(n):
		temp_mat=np.array(mat_cre_np[i:i+k,j:j+k])
		temp_max=max(left_right(temp_mat),up_down(temp_mat),dia_up(temp_mat),dia_down(temp_mat))
		if max_product<temp_max:
			max_product=temp_max
			final_mat=temp_mat
print(max_product)
print(final_mat)
