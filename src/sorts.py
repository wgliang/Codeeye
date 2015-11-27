import sys,os,time,commands  
from operator import itemgetter
import operator

#Get val separated by blank
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

#Sort file by lines
def lines_sort(data):
	res = sorted(data, key=operator.itemgetter('lines'))
	print res

#Sort file by date
def date_sort(data):
	res = sorted(data, key=operator.itemgetter('date'))
	print res

#Sort file by size
def size_sort(data):
	res = sorted(data, key=operator.itemgetter('size'))
	print res

#Sort file by type-count
def type_count_sort():
	pass

#Sort file by type-indiv
def type_indiv_sort():
	pass