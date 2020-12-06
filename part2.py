# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 03:35:08 2020

@author: Rob
"""

file = open('input.txt', 'r')
totalcount = 0
linecount = 0
dictionary = {}
for line in file:
	if line == '\n':
		values = list(dictionary.values())
		for i in values:
			if i == linecount:
				totalcount += 1
		linecount = 0
		dictionary.clear()
		values.clear()
		continue
	for i in line:
		if i!= '\n':
			if i in dictionary:
				dictionary[i] +=1
			else:
				dictionary[i] = 1
	linecount += 1
else:
	values = list(dictionary.values())
	for i in values:
		if i == linecount:
			totalcount += 1
print(totalcount)
file.close()