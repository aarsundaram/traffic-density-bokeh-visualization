import bokeh
import pandas
import time
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, save, show
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure

df1 = pandas.read_csv('n1_trucks.csv')
print(df1.head())

hourwise = []
for i in df1['hour'].unique():
    hourwise.append(df1.loc[df1['hour'] == i])

time.sleep(2)
# Set up data

x = hourwise[0]['source']
y = hourwise[0]['number']

source = ColumnDataSource(data=dict(x=x, y=y))

# Set up plot
plot = figure(y_range='y',plot_height=400, plot_width=800, title="my sine wave",
              tools="crosshair,pan,reset,save,wheel_zoom")

# plot.hbar(y=[1, 2, 3], height=0.5, left=0, right=[1,2,3], color="#CAB2D6")
plot.hbar(y='y', height=0.5, left=0, right='x', source=source, color="#CAB2D6")
# Set up widgets
text = TextInput(title="title", value='my sine wave')

hour1 = Slider(title="hour", value=0, start=0, end=96, step=1)


# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value


text.on_change('value', update_title)


def update_data(attrname, old, new):

    # Get the current slider values
    # a = amplitude.value
    h = hour1.value

    # Generate the new plot
    x = hourwise[h]['source']
    y = hourwise[h]['number']

    source.data = dict(x=x, y=y)


hour1.on_change('value', update_data)

# Set up layouts and add to document
inputs = column(hour1,text)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Sliders"