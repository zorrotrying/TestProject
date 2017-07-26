# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:20:21 2017

@author: zouro2
"""

import pandas as pd
import numpy as np
import re


def Fileprocess(filepath, StartLine, SheetName, EmptyLineNum, OutFilepath):
    skiprows = StartLine - 1
    xlsfile = pd.ExcelFile(filepath)
    df = pd.read_excel(xlsfile,sheetname=SheetName,skiprows=skiprows, header=1)
    df3 = df[df['Well'].apply(lambda x: type(x) in [int, np.int64, float, np.float64])][['CT','Target Name','Sample Name']].dropna()
    df3['CT'] = pd.to_numeric(df3['CT'], errors='coerce')
    
    TarNameList = df3['Target Name'].unique()
    SamNameList = df3['Sample Name'].unique()
    
    
    DFall = pd.DataFrame()
    for i in range(len(TarNameList)):
        DFnew = pd.DataFrame()
        for j in range(len(SamNameList)):
            data_list = df3[(df3['Target Name'] == TarNameList[i].encode('utf-8')) & (df3['Sample Name'] == SamNameList[j].encode('utf-8'))].CT.values
            try:
                DFnew[SamNameList[j].encode('utf-8')] = data_list
            except:
                data_except = pd.DataFrame({SamNameList[j].encode('utf-8'):data_list})
                DFnew = pd.concat([DFnew, data_except],axis=1)
        DFnew.index = [TarNameList[i].encode('utf-8')]*DFnew.shape[0]    
        DFnew.loc['average'] = DFnew.mean()
        DFnew = DFnew.append(pd.DataFrame(index=['']*EmptyLineNum, columns=DFnew.columns))
        #DFnew['TargetName'] = DFnew.index
        DFall = DFall.append(DFnew)
    
    # Sort the column name as Natural    
    ColList_sort = sorted(list(DFall.columns.values),
                          key=lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split('(\d+)', s)])
    
    DFfinal = DFall.reindex_axis(ColList_sort, axis=1)
    DFfinal.to_csv(OutFilepath)
