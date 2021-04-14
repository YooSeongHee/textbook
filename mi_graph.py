# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:08:17 2021

@author: user
"""

import math
import collections
import matplotlib.pyplot as plt
import matplotlib
import os, re
from matplotlib import font_manager, rc


word_frq_dict = collections.Counter()
ngram_frq_dict= collections.Counter()
N = 0

for root, dirs, files in os.walk(r'C:\Users\유성희\Desktop\script\text'):
	for fn in files:
		fp = os.path.join(root, fn)
		with open(fp, 'r', encoding = 'utf8', errors='ignore') as f:
			morph_list = []
			txt = f.read()
			N_list = []
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
						if re.search('/N', morph):
							Noun = morph.split('/')
							N_list.append(Noun[0])

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

	wordInfo = collections.Counter(N_list)

	font_location = "c:/Windows/fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=font_location).get_name()
	matplotlib.rc('font', family=font_name)

	plt.xlabel('주요 단어')
	plt.ylabel('빈도수')
	plt.grid(True)

	Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)[:20]
	Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)[:20]
	# plt.bar(range(len(Sorted_Dict_Values)), Sorted_Dict_Values, align='center', color="green")
	# plt.plot(range(len(Sorted_Dict_Values)), Sorted_Dict_Values, 'ro')
	# plt.plot(range(len(Sorted_Dict_Values)), Sorted_Dict_Values, 'bs')
	plt.plot(mi_val, Sorted_Dict_Values, 'g^')
# 	plt.xticks(range(len(Sorted_Dict_Values)), list(Sorted_Dict_Keys), rotation='50') # 주요단어의 기울기 조정 = rotation
	plt.show()






