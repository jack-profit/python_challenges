# _*_ coding:utf-8 _*_
import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)

    '''
    1.使用pandas选择数据
    2.转换为时间序列
    3.按季度重采样并排序

    目标：返回交易总量降序排名第2的季度的成交总量 sum()
    '''

    return second_volume

if __name__ == '__main__':
    quarter_volume()
