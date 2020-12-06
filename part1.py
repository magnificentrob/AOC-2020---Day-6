# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 02:45:39 2020

@author: Rob
"""
#6259
file = open('input.txt', 'r')
total_count = 0
yes = []
for line in file:
	if line == '\n':
		total_count += len(yes)
		yes.clear()
	for i in line:
		if i not in yes and i != '\n':
			yes.append(i)
else:
	total_count += len(yes)
file.close()
print(total_count)