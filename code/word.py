# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 02:31:52 2020

@author: 유성희
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os, re
import collections

for root, dirs, files in os.walk(r'..\script\text'):
	for fn in files:
		fp = os.path.join(root, fn)
		with open(fp, 'r', encoding = 'utf8', errors='ignore') as f:
			txt = f.read()
			N_list = []  #빈 리스트를 형태분석 불러오는 첫 단에다 만들어 줘야 했음. 이게 중요!!
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
						if re.search('/N', morph):
							Noun = morph.split('/')
							N_list.append(Noun[0])
			clue = np.array(Image.open('rabbit.jpg'))
			count = collections.Counter(N_list)
		wordcloud = WordCloud(font_path = 'C:/Windows/Fonts/malgun.ttf', background_color='white',colormap = "Accent_r",mask = clue, width=2000, height=3000).generate_from_frequencies(count)
		plt.figure(figsize=(15,15))
		plt.imshow(wordcloud)
# 		plt.axis('off')
# 		plt.savefig('rabbit_rev.png')
