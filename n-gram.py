#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:44:12 2020

@author: yukbi
"""
import collections

load = open(r'C:\Users\유성희\Desktop\script\운수 좋은 날.txt', encoding = 'utf8')
save = open(r'C:\Users\유성희\Desktop\script\result\result.txt', 'w', encoding = 'utf8')
lines = load.readlines()

word_frq_dict = collections.Counter()
ngram_frq_dict= collections.Counter()

for line in lines:
	line = line.strip()
	eojeol = line.split()

	word_list = []
	for word in eojeol:
		word_list.append(word)

	word_range = range(len(word_list) -1)
	for i in word_range:
		if word_list[i] and word_list[i+1]:
			ngram_frq_dict[(word_list[i], word_list[i+1])] += 1
			a = ngram_frq_dict.items()

sort = sorted(ngram_frq_dict.items(), key=lambda d:d[1], reverse=1)
save.write('{}'.format(sort))

for tup, frq in sort:
	n = tup[0], tup[1], frq
# 	save.write('{}\n'.format(n))








