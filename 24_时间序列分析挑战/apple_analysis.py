# _*_ coding:utf-8 _*_
import pandas as pd
from pandas import offsets, Series

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)

    target = pd.Series(list(data.Volume), index=data.Date) # 筛选数据
    target.index = pd.to_datetime(target.index) # 转换时间序列
    target = target.resample('Q').sum().sort_values() # 重采样并排序
    return target[-2]

if __name__ == '__main__':
    print(quarter_volume())
