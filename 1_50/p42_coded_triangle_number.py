'''Coded triangle number
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using triangle_words.txt , a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
import math
import string
import csv

refe_list=string.ascii_uppercase
filt_word=list()
with open('triangle_words.txt') as file_name:
	for line in csv.reader(file_name,delimiter=',',quotechar='"'):
		filt_word.extend(line)
trian_num=list()

max_word_score = len(max(filt_word, key=len))*26

n=1
while (n*(n+1))/2 <max_word_score:
	trian_num.append(n*(n+1)/2)
	n+=1
count=0	
for i in filt_word:
	if sum(refe_list.index(k)+1 for k in i) in trian_num:
		count+=1
		
print(count)
