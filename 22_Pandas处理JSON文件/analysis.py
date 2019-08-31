#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import json
import pandas as pds


def analysis(file, user_id):
    times = 0
    minutes = 0

    if user_id and file:
        with open(file) as f:
            data = pds.read_json(f)
            targets = data[data['user_id'] == user_id]
            times = targets.size
            minutes = targets['minutes'].sum()
    return times, minutes

if __name__ == '__main__':
    print(analysis('./user_study.json', 164830))
