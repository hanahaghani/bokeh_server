from bokeh.palettes import Category20_16
from bokeh.plotting import figure
from bokeh.models import (
    ColumnDataSource, TabPanel, Select, FixedTicker
)
from bokeh.layouts import Column, Row
from itertools import chain
import pandas as pd
import numpy as np

def route_tab(data):
    
    def prepare_source(origin, dest):
        subset = data[(data['origin'] == origin) & (data['dest'] == dest)]
        airlines = list(set(subset['name']))
        
        xs = []
        ys = []
        label_dict = {}

        for i, airline in enumerate(airlines):
            airline_flights = subset[subset['name'] == airline]
            xs.append(list(airline_flights['arr_delay']))
            ys.append([i] * len(airline_flights))
            label_dict[i] = airline

        # فلت‌کردن لیست‌ها
        xs = list(chain(*xs))
        ys = list(chain(*ys))

        return ColumnDataSource(data={'x': xs, 'y': ys}), label_dict

    def create_plot(src, label_dict):
        p = figure(title="نمودار تأخیر پرواز به تفکیک مسیر", height=600)
        p.scatter('x', 'y', source=src, size=12, color="blue", alpha=0.5)

        p.yaxis.ticker = FixedTicker(ticks=list(label_dict.keys()))
        p.yaxis.major_label_overrides = label_dict
        p.yaxis.axis_label = "ایرلاین‌ها"
        p.xaxis.axis_label = "تاخیر (دقیقه)"
        return p

    def update(attr, old, new):
        origin = origin_select.value
        dest = dest_select.value
        new_src, new_labels = prepare_source(origin, dest)
        source.data.update(new_src.data)
        plot.yaxis.ticker = FixedTicker(ticks=list(new_labels.keys()))
        plot.yaxis.major_label_overrides = new_labels

    # ساخت ویجت‌های انتخاب مبدا و مقصد
    origins = sorted(list(set(data['origin'])))
    destinations = sorted(list(set(data['dest'])))

    origin_select = Select(title='مبدأ', value=origins[0], options=origins)
    dest_select = Select(title='مقصد', value=destinations[0], options=destinations)

    # بارگذاری اولیه داده و نمودار
    source, label_dict = prepare_source(origin_select.value, dest_select.value)
    plot = create_plot(source, label_dict)

    # اتصال event handler
    origin_select.on_change('value', update)
    dest_select.on_change('value', update)

    layout = Row(Column(origin_select, dest_select), plot)
    tab = TabPanel(child=layout, title='مبدأ/مقصد')

    return tab