import matplotlib.pyplot as plt
import numpy as np
company=['Google','Amazon','Microsoft','Facebook']
revenue=[90,136,89,27]
profit=[25,45,36,56]
xpos=np.arange(len(company))
ypos=np.arange(len(company))

##COMMENT the codes of Virtical Bar chart  || Horizontal Bar chart when you intened to run the program

##virtical Bar chart
plt.xticks(ypos,company)
plt.bar(xpos-0.2, revenue,width=0.4,label='revenue')
plt.bar(xpos+0.2, profit, width=0.4,label='profit')
plt.legend()
plt.xlabel('Company')
plt.ylabel('Revenue')
plt.title('US Tech Stocks')
plt.show()

##Horizental Bar chart   Don't use width argument with barh

plt.yticks(ypos,company)
plt.barh(ypos-0.2, revenue,label='revenue')
plt.barh(ypos+0.2, profit,label='profit')
plt.legend()
plt.xlabel('Company')
plt.ylabel('Revenue')
plt.title('US Tech Stocks')
plt.show()