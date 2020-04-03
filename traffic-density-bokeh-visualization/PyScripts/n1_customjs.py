from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import Figure, output_file, show
import pandas
#get data
df1 = pandas.read_csv('n1_trucks.csv')
hourwise = []
for i in df1['hour'].unique():
    hourwise.append(df1.loc[df1['hour'] == i])


output_file("js_on_change.html")

x = hourwise[0]['source']
y = hourwise[0]['number']

source = ColumnDataSource(data=dict(x=x, y=y))

plot = Figure(y_range='y',plot_width=1200, plot_height=1200)
plot.hbar(y='y', left=0,right='x', source=source)

callback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var f = cb_obj.value
    var x = data['x']
    var y = data['y']
    x = hourwise[0]['source']
    y = hourwise[0]['number']
    source.change.emit();
""")

slider = Slider(start=0, end=96, value=0, step=1, title="hour")
slider.js_on_change('value', callback)

layout = column(slider, plot)
show(layout)