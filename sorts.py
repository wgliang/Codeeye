import sys,os,time,commands  
from operator import itemgetter
import operator
#TODO:Sort the code by lines
def sub_blank(str, target):
	i = 1
	while(i < target):
		index = str.find(' ')
		if(index >= 0):
			str = str[index+1:]
		else:
			return ''
		i = i + 1
	if(i != target):
		return ''
	index = str.find(' ')
	if(index >= 0):
		return str[:index]
	else:
		return str
	
def lines_sort(data):
	res = sorted(data, key=operator.itemgetter('lines'))
	print res

def date_sort():
	res = sorted(data, key=operator.itemgetter('date'))
	print res

def size_sort():
	res = sorted(data, key=operator.itemgetter('size'))
	print res

def type_count_sort():
	pass

def type_indiv_sort():
	pass