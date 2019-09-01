import pandas 

def analysis(file, user_id):
    data = pandas.read_json(file)
    targets = data[data['user_id'] == user_id].minutes
    targets = data[data.user_id == user_id].minutes
    return targets.count(), targets.sum()
