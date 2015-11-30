import matplotlib  
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt

data=[33,25,20,12,10]
plt.figure(num=1, figsize=(8,6))
plt.axes(aspect=1)
plt.title('Plot 3', size=14)
label = ['Group 1','Group 2','Group 3','Group 4','Group 5']
plt.pie(data, labels=label, autopct='%d%%')
plt.savefig('plot3.pdf', format='pdf')