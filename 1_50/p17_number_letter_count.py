#count the number of letter used in number from 1 to n
# we will use inflect lib
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage'''

import inflect
import time
n=int(input())
initial=time.time()
k=inflect.engine()
total_letter=0
for i in range(1,n+1):
	temp_num=k.number_to_words(i)
	temp_num=temp_num.replace(" ","")
	temp_num=temp_num.replace("-","")
	total_letter+=len(temp_num)
print(total_letter)
print(time.time()-initial)
