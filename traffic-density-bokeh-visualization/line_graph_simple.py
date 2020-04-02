from bokeh.plotting import figure, output_file, save, show
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
import pandas as pd 

x=[1,2,3,4,5,6]
y=[24,7,8,1,10,2]

output_file('trial.html')

p=figure(
    title="example"
)

p.line(x,y,legend='test',line_width=3)

show(p)
