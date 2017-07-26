# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 10:14:20 2017

@author: zouro2
"""

import pandas as pd

s = pd.Series([1,2,3,'abc','hh','ff'], index = ['a','a','b','c','d','f'])


data = {'state':['Ohino','Ohino','Ohino','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]}


df = pd.DataFrame(data, index=['one','two','three','four','five'], columns=['year','state','pop','columnNoData'])

state = ['state','year']
df.reindex(index=['one','two','three','ddd'], columns = state)




