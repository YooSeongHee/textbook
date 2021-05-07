# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:56:44 2020

@author: yukbi
"""

import os
import math
import collections
import re

word_frq_dict = collections.Counter()
ngram_frq_dict= collections.Counter()
N = 0

for root, dirs, files in os.walk(r'..\script\text'):
	print(dirs)
	for fn in files:
		fp = os.path.join(root, fn)
		with open(fp, 'r', encoding = 'utf8', errors='ignore') as f:
			morph_list = []
			txt = f.read()
			for para in re.findall("<body>(.*?)</body>", txt, re.S):
				para = para.strip()
				para_split = para.split('\n')
				for line in para_split:
					cols = line.split('\t')
					try:
						tagged_ej=cols[2]
					except:
						continue
					tagged_ej = tagged_ej.replace(' ', '')
					tagged_split = tagged_ej.split('+')
					for morph in tagged_split:
						N+=1
						morph_list.append(morph)
						word_frq_dict[morph]+=1

		for i in range(len(morph_list) -1):
			if re.search('/NN[GBP]', morph_list[i]) and re.search('/NN[GBP]', morph_list[i+1]):
				ngram_frq_dict[(morph_list[i], morph_list[i+1])] += 1

with open(r'C:\Users\유성희\Desktop\script\result\calculate.txt', "w", encoding='utf8') as outF:
	sort = sorted(ngram_frq_dict.items(), key=lambda d:d[1], reverse=1)
	for tup, frq in sort:
		w1=tup[0]
		w2=tup[1]
		p_xy=frq/N
		p_x=word_frq_dict[w1]/N
		p_y=word_frq_dict[w2]/N
		mi_val =math.log(p_xy/(p_x*p_y), 2)
		outF.write("{}\t{}\t{}\t{}\n". format(w1, w2, frq, mi_val))
