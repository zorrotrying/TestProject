# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 16:33:36 2017

@author: zouro2
"""

import pandas as pd

xlsfile = pd.ExcelFile('Test-1.xls')
df = pd.read_excel(xlsfile,sheetname='Results')
