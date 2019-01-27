'''Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?'''
def reverse_join(str_input):
	return "".join(sorted(str_input))

def comparision(n):
	return n=='123456789'

n=int(input())
num_list=list()
for i in range(1,n+1):
	temp_num=str(i)
	num=1
	while len(temp_num)<9:
		num+=1
		temp_num+=str(i*num)
	if comparision(reverse_join(temp_num)) and num>1:
		num_list.append(int(temp_num))
print(max(num_list))
	
