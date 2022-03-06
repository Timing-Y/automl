import pandas as pd
import os

def workif( type , num):
    root = os.getcwd()
    path = root + '/' + 'workif' + '.xlsx'

    if (os.path.isfile(path)):
        workif = pd.read_excel(path)
        workif_list = workif[0].tolist()
    else:
        workif_list = ["0"]
    if type == 'read':
        state = workif_list[0]
    elif type == 'write':
        workif_list[0] = num
        state = workif_list[0]

    workif_list_df = pd.DataFrame(workif_list)
    workif_list_df.to_excel(path, header=True, index=None)  # , startrow=len(old))

    return state
