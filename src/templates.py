import matplotlib  
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt
import oper

labels = ['C++', 'C', 'PHP', 'Python', 'Go', 'JavaScript', 'Shell', 'Java', 'HTML']

#shanxing
def sector(data, name):
	plt.cla()
	plt.subplot(8,1,1)
	plt.figure(num=1, figsize=(8,6))
	plt.axes(aspect=1)
	plt.title('Programming language-sector', size=14)
	plt.pie(data, labels=labels, autopct='%d%%')
	plt.savefig(name + '.pdf', format='pdf')
	plt.close()

#zhexian
def broken(date, data, name):
	plt.cla()
	plt.plot(date, data)
	plt.savefig(name + '.pdf', format='pdf')
	plt.close()
def bar(left, height, name):
	plt.cla()
	plt.bar(left, height)
	plt.savefig(name + '.pdf', format='pdf')
	plt.close()



