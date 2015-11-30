import matplotlib  
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt

labels = ['C++', 'C', 'PHP', 'Python', 'Go', 'JavaScript', 'Shell', 'Java', 'HTML']
#shanxing
def sector(data):
	print data
	plt.figure(num=1, figsize=(8,6))
	plt.axes(aspect=1)
	plt.title('Programming language-sector', size=14)
	plt.pie(data, labels=labels, autopct='%d%%')
	plt.savefig('sector_lines.pdf', format='pdf')

#zhexian
def broken():
	pass

