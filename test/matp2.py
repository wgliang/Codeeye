import matplotlib  
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt

mu = 0.0
sigma = 2.0
data= [20,45,65,76,6,34,43,54,65,7,89,0,8,64,33,123]
samples = np.random.normal(loc=mu, scale=sigma, size = 1000)
plt.figure(num=1, figsize=(8,6))
plt.title('Plot 2', size = 14)
plt.xlabel('value', size = 14)
plt.ylabel('counts', size=14)

plt.hist(data, bins=40, range=(-10,10))
plt.text(-9, 100, r'$\mu$ = 0.0, $\sigma$ = 2.0', size = 16)
plt.savefig('plot2.pdf', format = 'pdf')

