import matplotlib.pyplot as plt
import time
import random
import pandas
 
xdata = []

 #trucks 
df1=pandas.read_csv('createtrucks.csv',sep=';')
hourwise1=[] 
for i in df1['Time'].unique():
    hourwise1.append(df1.loc[df1['Time']==i])
ydata1 = []

#destroyed vehicles
df2=pandas.read_csv('destroyedvehicles.csv',sep=';')
hourwise2=[]
for k in df2['Time'].unique():
    hourwise2.append(df2.loc[df2['Time']==k])
ydata2=[] 

#cars
df3=pandas.read_csv('createcars.csv',sep=';')
hourwise3=[]
for l in df3['Time'].unique():
    hourwise3.append(df3.loc[df3['Time']==l])
ydata3=[] 

#buses
df4=pandas.read_csv('createbuses.csv',sep=';')
hourwise4=[]
for m in df4['Time'].unique():
    hourwise4.append(df4.loc[df4['Time']==m])
ydata4=[] 

plt.show()
 
axes = plt.gca()
axes.set_xlabel('Road Segments')
axes.set_ylabel('Vehicle Density')
axes.set_xlim(0, 69)
axes.set_ylim(0,300)
line1, = axes.plot(xdata, ydata1, 'r*-',label='truck')
line2, = axes.plot(xdata, ydata2, 'b+-',label='destroyed')
line3, = axes.plot(xdata, ydata3, 'g*-',label='cars')
line4, = axes.plot(xdata, ydata4, 'y*-',label='buses')

axes.set_xticks(list(range(0, 69, 2)))
axes.legend()


#loop
for hr in range(0,96):
    xdata = list(range(0,69))
    line1.set_xdata(xdata)
    line2.set_xdata(xdata)
    line3.set_xdata(xdata)
    line4.set_xdata(xdata)

    #trucks
    ydata1= hourwise1[hr]['Trucks']
    line1.set_ydata(ydata1)
    
    #destroyed
    ydata2=hourwise2[hr]['DestroyVehicles']
    line2.set_ydata(ydata2)
    
    #cars
    ydata3=hourwise3[hr]['Cars']
    line3.set_ydata(ydata3)

    #buses
    ydata4=hourwise4[hr]['Buses']
    line4.set_ydata(ydata4)

    #dynamically display hour
    axes.set_title('Hour= '+ str(hr))
    plt.draw()
    plt.pause(1e-17)
    time.sleep(0.01)

#  add this if you don't want the window to disappear at the end
plt.show()