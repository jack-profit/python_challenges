#!/usr/bin/env python3

# _*_ coding:utf-8 _*_

from functools import reduce

pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]

# fan hui da yu deng yu 96 de yuan su
def a(data):
    if data[1] >= 96:
        return True
    else:
        return False

# jiang zi fu chuan zhuan cheng xiao xie
def b(i, j):
    result = []
    print(j)
    print(i, end='...')
    result.append(j[0].lower())
    return result


if __name__ == '__main__':

    # filter guo lv
    # print(list(filter(a, pp)))

    # reduce 
    print(reduce(b, pp))
