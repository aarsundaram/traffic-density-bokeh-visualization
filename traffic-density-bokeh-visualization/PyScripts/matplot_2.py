import matplotlib.pyplot as plt
import time
import random
import pandas
 
df1=pandas.read_csv('n1_trucks.csv')
hourwise=[]
for i in df1['hour'].unique():
    hourwise.append(df1.loc[df1['hour']==i])

xdata = 0
ydata = 1
 
plt.show()
 
axes = plt.gca()
axes.set_xlim(0, 69)
axes.set_ylim(0,900)
line1, = axes.plot(xdata, ydata, 'r*-')
line2, = axes.plot(xdata, ydata, 'b+-')
axes.set_xticks(list(range(0, 69, 2)))
for hr in range(0,96):
    ydata1=hourwise[hr]['number']
    xdata = list(range(0,69))
    ydata2=hourwise[hr]['number']+10
    line1.set_xdata(xdata)
    line1.set_ydata(ydata1)
    line2.set_xdata(xdata)
    line2.set_ydata(ydata2)
    plt.draw()
    plt.pause(1e-17)
    time.sleep(0.01)

#  add this if you don't want the window to disappear at the end
plt.show()