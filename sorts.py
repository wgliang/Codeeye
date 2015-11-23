import sys,os,time,commands  
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
	
def lines_sort():
	pass

def date_sort():
	pass

def size_sort():
	pass

def type_count_sort():
	pass

def type_indiv_sort():
	pass

if(__name__=='__main__'):  
	print sub_blank('grhg', 2)