import matplotlib.pyplot as plt
import time
import random
import pandas
 
df1=pandas.read_csv('n1_trucks.csv')
hourwise=[]
for i in df1['hour'].unique():
    hourwise.append(df1.loc[df1['hour']==i])

xdata = []
ydata = []
 
plt.show()
 
axes = plt.gca()
axes.set_xlim(1, 100)
axes.set_ylim(0,900)
line, = axes.plot(xdata, ydata, 'r-')
for hr in range(0,96):
    ydata=hourwise[hr]['number']
    xdata = list(range(0,69))
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    plt.draw()
    plt.pause(1e-17)
    time.sleep(0.01)

#  add this if you don't want the window to disappear at the end
plt.show()