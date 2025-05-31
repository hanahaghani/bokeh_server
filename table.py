from bokeh.palettes import Category20_16
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource , TabPanel , Tabs ,Slider, RangeSlider,CheckboxGroup,CheckboxButtonGroup 
from bokeh.layouts import Column , Row 
from bokeh.models.widgets import TableColumn,DataTable
import pandas as pd 
import numpy as np   

def table_tab(data):
    d= data.groupby('name')['arr_delay'].describe()
    d['mean']=d['mean'].round(2)
    d['std']=d['std'].round(2)
    
    c=ColumnDataSource(d)
    flights_table=DataTable(
        source=c,
        columns=[
            TableColumn(field='name',title='نام ایرلاین'),
            TableColumn(field='count',title='تعداد پرواز'),
            TableColumn(field='mean',title='میانگین تاخیر'),
            TableColumn(field='std',title='انحراف استاندارد'),
            TableColumn(field='min',title='کمینه تاخیر'),
            TableColumn(field='25%',title='25%'),
            TableColumn(field='50%',title='50%'),
            TableColumn(field='75%',title='75%'),
            TableColumn(field='max',title='بیشینه تاخیر')
        ],
        width=1400
    )
    tab=TabPanel(child=flights_table,title='خلاصه تاخیر ها')
    return tab
    