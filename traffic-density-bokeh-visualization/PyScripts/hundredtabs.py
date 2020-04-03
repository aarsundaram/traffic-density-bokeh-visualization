
import bokeh
import pandas
import time
#import matplotlib
from bokeh.plotting import figure, output_file, save, show
import bokeh.models as bkm
df1=pandas.read_csv('n1_trucks.csv')
hourwise=[]
for i in df1['hour'].unique():
    hourwise.append(df1.loc[df1['hour']==i])

j=0
while j<96:
    source1=hourwise[j]['source']
    numbers1=hourwise[j]['number']
    yr= range(200)
    p=figure(
        y_range=source1,
        #x_range=bkm.DataRange1d(end=300),
        title='Hour='+str(j),
        plot_width=800,
        plot_height=800,
        x_axis_label='segmentname'
        )


    p.hbar(
        y=source1,
        right=0,
        left=numbers1,
        height=0.2,
        color='red',
        fill_alpha=0.5
    )
    j+=1

    save(p)
    output_file('hundredtabs.html')
    time.sleep(0.5)
    
