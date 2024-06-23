import matplotlib.pyplot as plt
import numpy as np

blood_suger=[113,85,90,150,149,88,93,115,135,77,82,129]

#plt.hist(blood_suger,rwidth=0.95,bins=3)
#plt.hist(blood_suger,bins=[80,100,125,150],rwidth=0.95,color='red',histtype='step')

#different datasets
blood_suger_man=[113,85,90,150,149,88,93,115,135,77,82,129]
blood_suger_women=[67,98,89,120,133,150,84,69,89,79,120,112,100]
plt.hist([blood_suger_man,blood_suger_women],bins=[80,100,125,150],rwidth=0.95,color=['red','yellow'],label=['man','women'],orientation='horizontal')
plt.legend(loc='best')
plt.xlabel('suger range')
plt.ylabel('Total number of patients')
plt.title('blood suger analysis')
plt.show()