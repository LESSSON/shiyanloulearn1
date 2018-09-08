#-*- coding:utf-8 -*-
#!usr/bin/env python

import json

def analysis(filename, user_id):
    times = 0
    minutes = 0

    try:
        with open(filename, 'r') as file:
            data = json.loads(file.read())
    except:
        return times, minutes

        if !t.get(user_id, 0):
            times = times + 1
            minutes = minutes + t[user_id]


    return times, minutes
