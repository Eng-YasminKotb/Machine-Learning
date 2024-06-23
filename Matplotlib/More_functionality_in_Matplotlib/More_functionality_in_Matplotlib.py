import matplotlib.pyplot as plt
import numpy as np
##Axes labels
day=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,47,49,46]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,48,46,40,42,41]

plt.plot(day,max_t, label="Max")
plt.plot(day,min_t, label="Min")
plt.plot(day,avg_t, label="Avg")
plt.xlabel("day")
plt.ylabel("temperature")
plt.title("weather")

##plt.legend()
plt.legend(loc="best", shadow=True, fontsize="small")

##plt.grid()
plt.grid()
plt.show()

