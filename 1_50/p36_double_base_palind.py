'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
list_num=list()
n=int(input())
for j in range(1,n):
	z=str(j)
	# Checking the given number is panlindrome
	for k in range(len(z)):
		if z[k]!=z[-k-1]:
			break
	else:
		#checking the binary form of the panlindrom number is palindrome
		z_bina=f"{j:b}"
		for l in range(len(z_bina)):
			if z_bina[l]!=z_bina[-l-1]:
				break
		else:
			list_num.append(j)
			
print(sum(list_num))
