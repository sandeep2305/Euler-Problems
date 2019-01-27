# largest palindrome Number
#n=int(input()) #num of digits 
'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''
def isPalindrome(str_input):
	return str_input=="".join(reversed(str_input))
list_num=[]
for i in range(101,1000):
	for j in range(101,1000):
		z=str(i*j)
		if isPalindrome(z):
			list_num.append(int(z))
			
print(max(list_num))
