# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:16:36 2021

@author: user
"""
import json

with open(r'..\script\text\practice.JSON', 'r', encoding = 'utf8') as f:
 	txt = json.load(f)
 	for document in txt['document']:
 		for sentence in document['sentence']:
 			id_ = sentence['id']
 			form = sentence['form']
 			for word in sentence['word']:
 				word_form = word['form']
 				anal = word['anal']
 				print(word_form, anal)

