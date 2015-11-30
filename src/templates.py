import matplotlib  
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt
import oper

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
def broken(date, data, name):
	# plt.figure(num=1, figsize=(8,6))
	# plt.axes(aspect=1)
	# plt.title('lines-zhexiantu', size=14)
	print date
	print 
	print data
	plt.plot(date, data)
	plt.savefig(name + '.pdf', format='pdf')



