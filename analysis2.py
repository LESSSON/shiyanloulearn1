#-*- coding:utf-8 -*-
#!usr/bin/env python

import json
import pandas as pd
from pandas import Series, DataFrame

def analysis(file, user_id):
    times = 0
    minutes = 0

    try:
        date = pd.read_json(file,orient='values',encoding='utf-8')
    except:
        return times, minutes
    
    df = DataFrame(date)
    times = df[df['user_id'] == user_id].shape[0]
    minutes = df[df['user_id'] == user_id]['minutes'].sum()




    return times, minutes

#a = 'user_study.json'
#x = analysis(a,199071)
#print(x)

