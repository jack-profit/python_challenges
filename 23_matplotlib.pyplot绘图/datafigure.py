import pandas as pds
from pandas import DataFrame
import matplotlib.pyplot as plt

def get_data_json_file(file):
    data = pds.read_json(file)
    result = []
    set_ids = set(data.user_id) # 获取全部ID并去重
    for v in set_ids:
        item = {
            'id': v,
            'time': data[data.user_id ==v].minutes.sum()
        }
        result.append(item)
    return result

def data_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')

    DataFrame(get_data_json_file('./user_study.json')).plot()
    plt.show()
    return ax

if __name__ == '__main__':
    data_plot()

