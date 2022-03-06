import pandas as pd
import os

def organize( newid ,Lname):
    newid_t = []
    for i in newid:
        newid_t.append(int(i))
    root = os.getcwd()
    if Lname == 'NBA':
        path_wait = root + '/' + 'Bwait' + '.xlsx'
        path_done = root + '/' + 'Bdone' + '.xlsx'
        path_delay = root + '/' + 'Bdelay' + '.xlsx'
    elif Lname == 'CBA':
        path_wait = root + '/' + 'Bwait' + '.xlsx'
        path_done = root + '/' + 'Bdone' + '.xlsx'
        path_delay = root + '/' + 'Bdelay' + '.xlsx'
    elif Lname == 'FOOTBALL':
        path_wait = root + '/' + 'Fwait' + '.xlsx'
        path_done = root + '/' + 'Fdone' + '.xlsx'
        path_delay = root + '/' + 'Fdelay' + '.xlsx'
    # path_wait = root + '\\' + 'Fwait' + '.xlsx'
    # path_done = root + '\\' + 'Fdone' + '.xlsx'


    if(os.path.isfile(path_wait)):
        wait_sp = pd.read_excel(path_wait)
        wait_sp_list = wait_sp[0].tolist()
    else:
        wait_sp_list = []
    if (os.path.isfile(path_done)):
        done_sp = pd.read_excel(path_done)
        done_sp_list = done_sp[0].tolist()
    else:
        done_sp_list = []
    if (os.path.isfile(path_delay)):
        delay_sp = pd.read_excel(path_delay)
        delay_sp_list = delay_sp[0].tolist()
    else:
        delay_sp_list = []

    wait_sp_list.extend(newid_t)
    new_wait_sp = ["0"]
    for i in wait_sp_list:
        if i not in done_sp_list:
            if i not in new_wait_sp:
                new_wait_sp.append(i)
    all_wait_sp = ["0"]
    for i in wait_sp_list:
        if i not in done_sp_list:
            if i not in delay_sp_list:
                if i not in all_wait_sp:
                    all_wait_sp.append(i)

    new_wait_sp_df = pd.DataFrame(new_wait_sp)
    new_wait_sp_df = new_wait_sp_df.drop(labels=0)
    del new_wait_sp[0]
    del all_wait_sp[0]
    new_wait_sp_df.to_excel(path_wait, header=True, index=None)#, startrow=len(old))

    return all_wait_sp

def spider_done( id ,Lname):
    root = os.getcwd()
    print("spider_done")
    if Lname == 'NBA':
        path_done = root + '/' + 'Bdone' + '.xlsx'
    elif Lname == 'CBA':
        path_done = root + '/' + 'Bdone' + '.xlsx'
    elif Lname == 'FOOTBALL':
        path_done = root + '/' + 'Fdone' + '.xlsx'
    #path_done = root + '\\' + 'Fdone' + '.xlsx'
    if (os.path.isfile(path_done)):
        done_sp = pd.read_excel(path_done)
        done_sp_list = done_sp[0].tolist()
    else:
        done_sp_list = ["0"]
    # done_sp = pd.read_excel(path_done)
    # done_sp_list = done_sp[0].tolist()
    done_sp_list.append(id)
    new_done_sp_df = pd.DataFrame(done_sp_list)
    new_done_sp_df.to_excel(path_done, header=True, index=None)  # , startrow=len(old))
    return

def spider_delay( id ,Lname):
    root = os.getcwd()
    print("spider_delay")
    if Lname == 'NBA':
        path_delay = root + '/' + 'Bdelay' + '.xlsx'
    elif Lname == 'CBA':
        path_delay = root + '/' + 'Bdelay' + '.xlsx'
    elif Lname == 'FOOTBALL':
        path_delay = root + '/' + 'Fdelay' + '.xlsx'
    #path_delay = root + '\\' + 'Fdelay' + '.xlsx'
    if (os.path.isfile(path_delay)):
        done_sp = pd.read_excel(path_delay)
        done_sp_list = done_sp[0].tolist()
    else:
        done_sp_list = ["0"]
    # done_sp = pd.read_excel(path_done)
    # done_sp_list = done_sp[0].tolist()
    done_sp_list.append(id)
    new_done_sp_df = pd.DataFrame(done_sp_list)
    new_done_sp_df.to_excel(path_delay, header=True, index=None)  # , startrow=len(old))
    return

def delay_clear(Lname):
    root = os.getcwd()
    print("delay_clear")
    if Lname == 'NBA':
        path_delay = root + '/' + 'Bdelay' + '.xlsx'
    elif Lname == 'CBA':
        path_delay = root + '/' + 'Bdelay' + '.xlsx'
    elif Lname == 'FOOTBALL':
        path_delay = root + '/' + 'Fdelay' + '.xlsx'
    done_sp_list = ["0"]
    new_done_sp_df = pd.DataFrame(done_sp_list)
    new_done_sp_df.to_excel(path_delay, header=True, index=None)  # , startrow=len(old))
    return
