import pandas as pds
import matplotlib.pyplot as plt


def data_plot():
    data = pds.read_json('./user_study.json')

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')

    df = data.groupby('user_id').sum()
    ax.plot(df.index, df.minutes)
    # data.groupby('user_id').sum().plot()
    plt.show()
    return ax

if __name__ == '__main__':
    data_plot()
