from bokeh.io import curdoc
from bokeh.models import Tabs
from os.path import dirname , join
import pandas as pd 
from hist import hist_tab
from table import table_tab
from route import route_tab

data = pd.read_csv('flights.csv', index_col=0).dropna()

tab_hist=hist_tab(data)
tab_table=table_tab(data)
tab_route= route_tab(data)
tabs=Tabs(tabs=[tab_hist,tab_table,tab_route])
curdoc().add_root(tabs)