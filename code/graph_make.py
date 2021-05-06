# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:33:56 2021

@author: user
"""
import matplotlib.pyplot as plt
import os, re
import collections
from matplotlib import font_manager, rc

for root, dirs, files in os.walk(r'C:\Users\유성희\Desktop\script\text'):
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

font_location = "c:/Windows/fonts/H2GTRM.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

plt.subplots(figsize=(8, 4)) #그래프 사이즈(inch)
plt.title('빈도 그래프')
plt.xlabel('주요 단어')
plt.ylabel('빈도수')
plt.grid(True)

wordInfo = collections.Counter(N_list)
frq = sorted(wordInfo.values(), reverse=True)[:20]
word = sorted(wordInfo, key=wordInfo.get, reverse=True)[:20]

"""
# 정렬
word = sorted(wordInfo.keys(), reverse=False)[:20]

# 그래프 색 변경 & 모양 변경
plt.bar(range(len(frq)), frq, align='center', color="g")
plt.plot(range(len(frq)), frq, 'ro')
plt.plot(range(len(frq)), frq, 'ys')
plt.plot(range(len(frq)), frq, 'mv')
"""

plt.plot(range(len(frq)), frq, 'b^')
plt.xticks(range(len(frq)), list(word), rotation='50') # 주요단어의 기울기 조정 = rotation
# plt.show()
# plt.tight_layout()
plt.savefig(r"C:\Users\유성희\Desktop\script\result\savefig_default.png")






















