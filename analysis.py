#-*- coding:utf-8 -*-
#!usr/bin/env python

import json

def analysis(filename, user_id):
    times = 0
    minutes = 0

    try:
        data = json.load(open(filename))
    except:
        return times, minutes

        if t['user_id'] = user_id:
            times = times + 1
            minutes = minutes + t[user_id]


    return times, minutes
