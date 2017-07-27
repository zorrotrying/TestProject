# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:02:16 2017

@author: zouro2
"""

import pandas as pd
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem

def ListSimilarity(file1, file2, fptype):
    PDtable1 = pd.read_csv(file1)
    PDtable2 = pd.read_csv(file2)
    
    Name1 = []
    Name2 = []
    Similarity = []
    
    for i in range(PDtable1.shape[0]):
    Name1_tmp = []
    Name2_tmp = []
    Sim_tmp = []
    
    for j in range(PDtable2.shape[0]):
        m1 = Chem.MolFromSmiles(PDtable1.iloc[i,1])
        m2 = Chem.MolFromSmiles(PDtable1.iloc[j,1])
        fp1 = AllChem.GetMorganFingerprint(m1,2)
        fp2 = AllChem.GetMorganFingerprint(m2,2)
        Sim_Tanimoto = DataStructs.TanimotoSimilarity(fp1,fp2)
        if Sim_Tanimoto >= 0.5:
            Name1_tmp_tmp = PDtable1.iloc[i,0]
            Name2_tmp_tmp = PDtable2.iloc[j,0]
            #Smiles1 = PDtable1.iloc[i,1]
            #Smiles2 = PDtable1.iloc[j,1]
            Similarity_tmp_tmp = Sim_Tanimoto
            Name1_tmp.append(Name1_tmp_tmp)
            Name2_tmp.append(Name2_tmp_tmp)
            Sim_tmp.append(Similarity_tmp_tmp)
    Name1.extend(Name1_tmp)
    Name2.extend(Name2_tmp)
    Similarity.extend(Sim_tmp)
    
    Sim_DF = pd.DataFrame(
        {'Name1':Name1,
         'Name2':Name2,
         'Similarity':Similarity})
    Sim_DF.to_csv('Result.csv', index = False)

    