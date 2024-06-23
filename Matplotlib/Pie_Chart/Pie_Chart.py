import matplotlib.pyplot as plt


exp_vals=[1400,600,300,410,250]
exp_labels=["Home Rent","Food","Phone/Internet Bill","Car", "Other Utilities"]
plt.axis("equal")
#you can use shadow parameter -->  shoadow=True
#The angle by which the start of the pie is rotated, counterclockwise from the x-axis.
plt.pie(exp_vals,labels=exp_labels,radius=0.95,autopct='%0.0f%%',explode=[0,0,0,0,0],startangle=45)
plt.show()