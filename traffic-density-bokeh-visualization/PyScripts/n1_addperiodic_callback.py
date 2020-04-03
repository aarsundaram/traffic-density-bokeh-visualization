import bokeh
import pandas
from bokeh.plotting import figure, output_file, save, show
from bokeh.io import curdoc

# df1 = pandas.DataFrame()
df1 = pandas.read_csv('n1_trucks.csv')
j=0
hourwise = []
for i in df1['hour'].unique():
    hourwise.append(df1.loc[df1['hour'] == i])
source1 = hourwise[0]['source']
numbers1 = hourwise[0]['number']

def n_function():
    source1 = hourwise[94]['source']
    numbers1 = hourwise[94]['number']
    

p = figure(
    y_range=source1,
    title='simple example',
    plot_width=800,
    plot_height=800,
    x_axis_label='segmentname'
)

p.hbar(
    y=source1,
    right=0,
    left=numbers1,
    height=0.4,
    color='red',
    fill_alpha=0.5
)


curdoc().add_periodic_callback(n_function, 200)
show(p)
