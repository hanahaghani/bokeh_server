from bokeh.palettes import Category20_16
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource , TabPanel , Tabs ,Slider, RangeSlider,CheckboxGroup,CheckboxButtonGroup 
from bokeh.layouts import Column , Row 
import pandas as pd 
import numpy as np   

def hist_tab(data):
    def md(s_data, rs=-60, re=120, bin=10):
        d = pd.DataFrame(columns=['proportion', 'left', 'right', 'f_proportion', 'f_interval', 'name', 'color'])
        r = re - rs
        for i, r_data in enumerate(s_data):
            subset = data[data['name'] == r_data]
            arr_hist, edge = np.histogram(subset['arr_delay'], bins=int(r / bin), range=(rs, re))
            arr_df = pd.DataFrame({
                'proportion': arr_hist / np.sum(arr_hist),
                'left': edge[:-1],
                'right': edge[1:]
            })
            arr_df['f_proportion'] = ['%0.5f' % p for p in arr_df['proportion']]
            arr_df['f_interval'] = ['%d to %d minutes' % (left, right) for left, right in zip(arr_df['left'], arr_df['right'])]
            arr_df['name'] = r_data
            arr_df['color'] = Category20_16[i]
            d = pd.concat([d, arr_df])  # اصلاح d.add
        d = d.sort_values(['name', 'left'])
        return ColumnDataSource(d)
    
    def mp(s_data):
        p = figure(width=700, height=700, title='تاخیر در پرواز')
        p.quad(source=s_data, bottom=0, top='proportion', left='left', right='right', color='color', fill_alpha=0.5, legend_field='name')
        return p
    
    def update(attr, old, new):
        checked = [chBox.labels[i] for i in chBox.active]
        ds = md(checked, rs=Range_slider.value[0], re=Range_slider.value[1], bin=slider.value)
        src.data.update(ds.data)  # این خط خیلی مهمه
    
    air_line = sorted(list(set(data['name'])))
    colors = sorted(list(Category20_16))
    
    chBox = CheckboxGroup(labels=air_line, active=[0, 1])
    slider = Slider(start=1, end=30, step=1, value=5, title='دانه‌بندی هیستوگرام')
    Range_slider = RangeSlider(start=-60, end=180, value=(-60, 120), step=5, title='بازه‌ی تاخیر')
    
    init_data = [chBox.labels[i] for i in chBox.active]
    src = md(init_data, rs=Range_slider.value[0], re=Range_slider.value[1], bin=slider.value)
    p = mp(src)
    
    chBox.on_change('active', update)
    slider.on_change('value', update)
    Range_slider.on_change('value', update)
    
    layout = Row(Column(chBox, slider, Range_slider), p)
    
    return TabPanel(child=layout,title='پنل هیستوگرام')