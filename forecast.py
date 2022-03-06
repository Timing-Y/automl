import pandas as pd
import os
from autogluon.tabular import TabularPredictor
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

close_time = 1200
alltimeflag = 0

my_sender = 'huozhihuiyi@126.com'  # 发件人邮箱账号
my_pass = 'WAVPQHXGLGUAYZXC'  # 发件人邮箱密码
my_user = '641678112@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail(data,time,state):
    ret = True
    try:

        message = MIMEMultipart()
        message['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = time  # 邮件的主题，也可以说是标题

        # 邮件正文内容
        if state == 1:
            message.attach(MIMEText(data, 'HTML', 'utf-8'))
        elif state == 2:
        # 构造附件1，传送当前目录下的 test.txt 文件
            att1 = MIMEText(open((str)(data), 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="1.xlsx"'
            message.attach(att1)

        server = smtplib.SMTP_SSL("smtp.126.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

def forecast(Lname):
    root = os.getcwd()  # 获取当前路径
    if Lname == 'NBA':
        path = root + '/' + 'NBAdata' + '.xlsx'
    elif Lname == 'CBA':
        path = root + '/' + 'CBAdata' + '.xlsx'
    elif Lname == 'FOOTBALL':
        path = root + '/' + 'Fdata' + '.xlsx'

    train_data_all = pd.read_excel(path)
    train_data_all.fillna(0)

    label_n = ['6', '7', '8', '10']
    label_zk = 9
    label_dx = 11
    for i in label_n:
        train_data_all = train_data_all.drop(columns=int(i))

    test_data = []
    test_data = pd.DataFrame(train_data_all)
    out_finish = []
    out_finish = pd.DataFrame()
    out_finish['编号'] = test_data[0]
    out_finish['时间'] = test_data[1]
    out_finish['联赛'] = test_data[2]
    out_finish['主队'] = test_data[3]
    out_finish['客队'] = test_data[4]
    out_finish['状态'] = test_data[5]
    out_finish['zk_f'] = test_data[9]
    out_finish['dx_f'] = test_data[11]
    test_data.drop(index=(test_data.loc[(test_data[5] == "完")].index), inplace=True)
    #print(test_data)
    if ((len(test_data)) == 0):
        return
    if Lname == 'NBA':
        save_path_zk_D = ['agModels-predictClassNBAzk_D', 'agModels-predictClassNBAdx_D']
        save_path_zk_3D = ['agModels-predictClassNBAzk_3D', 'agModels-predictClassNBAdx_3D']
        save_path_zk_W = ['agModels-predictClassNBAzk_W', 'agModels-predictClassNBAdx_W']
        save_path_zk_M = ['agModels-predictClassNBAzk_M', 'agModels-predictClassNBAdx_M']
        save_path_zk_A = ['agModels-predictClassNBAzk_A', 'agModels-predictClassNBAdx_A']
    elif Lname == 'CBA':
        save_path_zk_D = ['agModels-predictClassCBAzk_D', 'agModels-predictClassCBAdx_D']
        save_path_zk_3D = ['agModels-predictClassCBAzk_3D', 'agModels-predictClassCBAdx_3D']
        save_path_zk_W = ['agModels-predictClassCBAzk_W', 'agModels-predictClassCBAdx_W']
        save_path_zk_M = ['agModels-predictClassCBAzk_M', 'agModels-predictClassCBAdx_M']
        save_path_zk_A = ['agModels-predictClassCBAzk_A', 'agModels-predictClassCBAdx_A']
    elif Lname == 'FOOTBALL':
        save_path_zk_D = ['agModels-predictClassFzk_D', 'agModels-predictClassFdx_D']
        save_path_zk_3D = ['agModels-predictClassFzk_3D', 'agModels-predictClassFdx_3D']
        save_path_zk_W = ['agModels-predictClassFzk_W', 'agModels-predictClassFdx_W']
        save_path_zk_M = ['agModels-predictClassFzk_M', 'agModels-predictClassFdx_M']
        save_path_zk_A = ['agModels-predictClassFzk_A', 'agModels-predictClassFdx_A']

    save_path_list = [save_path_zk_D, save_path_zk_3D, save_path_zk_W, save_path_zk_M, save_path_zk_A]

    out_pred = []
    out_pred = pd.DataFrame()
    out_pred['编号'] = test_data[0]
    out_pred['时间'] = test_data[1]
    out_pred['联赛'] = test_data[2]
    out_pred['主队'] = test_data[3]
    out_pred['客队'] = test_data[4]
    out_pred['状态'] = test_data[5]

    for i in range(len(save_path_list)):
        save_path_zk = save_path_list[i][0]
        save_path_dx = save_path_list[i][1]
        test_data_nolab = test_data.drop(columns=[label_zk])
        test_data_nolab = test_data_nolab.drop(columns=[label_dx])

        predictor = TabularPredictor.load(save_path_zk)
        y_pred = predictor.predict(test_data_nolab)
        # print(y_pred)
        out_pred[save_path_zk] = y_pred
        # print(out_pred)
        predictor = TabularPredictor.load(save_path_dx)
        y_pred = predictor.predict(test_data_nolab)
        # print(y_pred)
        out_pred[save_path_dx] = y_pred
    #print(out_pred)

    #for i in range(len(save_path_list)):
    out_pred['sum_zk'] = out_pred[
        [save_path_list[1][0], save_path_list[2][0], save_path_list[3][0],
         save_path_list[4][0]]].sum(axis=1)#save_path_list[0][0],
    out_pred['sum_dx'] = out_pred[
        [save_path_list[1][1], save_path_list[2][1], save_path_list[3][1],
         save_path_list[4][1]]].sum(axis=1)#save_path_list[0][1],

    out_pred['zk'] = out_pred.apply(lambda x: '主' if x['sum_zk'] >= 4 else '客' if x['sum_zk'] <= -4 else 0,
                                    axis=1)
    out_pred['dx'] = out_pred.apply(lambda x: '大' if x['sum_dx'] >= 4 else '小' if x['sum_dx'] <= -4 else 0,
                                    axis=1)

    if Lname == 'NBA':
        path_out_pred = root + '/' + 'NBAout_pred' + '.xlsx'
    elif Lname == 'CBA':
        path_out_pred = root + '/' + 'CBAout_pred' + '.xlsx'
    elif Lname == 'FOOTBALL':
        path_out_pred = root + '/' + 'Fout_pred' + '.xlsx'

    if (os.path.isfile(path_out_pred)):
        Odata = pd.read_excel(path_out_pred)
        out_pred = Odata.append(out_pred, ignore_index=True)
    out_pred['编号'] = out_pred['编号'].astype('str')

    out_pred = out_pred.drop_duplicates(subset=['编号'], keep='last')
    out_pred.sort_values(by='时间', inplace=True)
    # result_df = result_df.sort_values(by='时间', ascending=True)
    # result_df = result_df.reset_index(drop=True)

    out_finish = out_finish[out_finish['状态'] == '完']
    num_finish_list = out_finish['编号'].values.tolist()
    out_pred['状态'] = out_pred.apply(lambda x: '完' if int(x['编号']) in num_finish_list else 'VS', axis=1)
    out_pred.to_excel(path_out_pred, index=None)

    time_now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    out_pred['diff'] = out_pred.apply(
        lambda x: time.mktime(time.strptime(str(x['时间']), "%Y-%m-%d %H:%M")) - time.mktime(
            time.strptime(str(time_now), "%Y-%m-%d %H:%M")),
        axis=1)
    if alltimeflag == 0:
        out_pred_now = out_pred[(out_pred['diff'] > -close_time) & (out_pred['diff'] < close_time)]
    else:
        out_pred_now = out_pred.copy()
        out_pred_now = out_pred_now[out_pred_now['状态'] != '完']
    out_pred_1 = out_pred_now[(out_pred_now['dx'] != 0) | (out_pred_now['zk'] != 0)]
    #print(out_pred_1)
    out_pred_1 = out_pred_1[["编号","时间", "联赛", "状态", "主队", "客队", "zk", "dx"]]

    ##概率
    out_pred_finish = out_pred[out_pred['状态'] == '完']
    pred_zkdf = []
    pred_dxdf = []
    #pred_df = pd.DataFrame(pred_df)
    for i in range(len(save_path_list)):
        save_path_zk = save_path_list[i][0]
        save_path_dx = save_path_list[i][1]
        out_pred_zk = out_pred_finish[-50:]
        y_test_zk_num = out_pred_zk['编号'].tolist()
        y_test_zk = []
        y_pred_zk = out_pred_zk[save_path_zk].tolist()
        for i in y_test_zk_num:
            if int(out_finish.loc[out_finish['编号'] == int(i)]['zk_f']) == 1:
                y_test_zk.append(1)
            elif int(out_finish.loc[out_finish['编号'] == int(i)]['zk_f']) == -1:
                y_test_zk.append(-1)
            else:
                y_test_zk.append(0)
        L = len(y_test_zk)
        N = 0
        for i in range(L):
            if y_test_zk[i] == y_pred_zk[i]:
                N += 1
            elif y_test_zk[i] == 0:
                L -= 1
        if L == 0 :
            L += 1
        pref_zk = float(N / L)
        pred_zkdf.append([save_path_zk,str(pref_zk)])
        #print(save_path_zk + ':' + str(pref_zk))

        out_pred_dx = out_pred_finish[-50:]
        y_test_dx_num = out_pred_dx['编号'].tolist()
        y_test_dx = []
        y_pred_dx = out_pred_dx[save_path_dx].tolist()
        for i in y_test_dx_num:
            if int(out_finish.loc[out_finish['编号'] == int(i)]['dx_f']) == 1:
                y_test_dx.append(1)
            elif int(out_finish.loc[out_finish['编号'] == int(i)]['dx_f']) == -1:
                y_test_dx.append(-1)
            else:
                y_test_dx.append(0)
        L = len(y_test_dx)
        N = 0
        for i in range(L):
            if y_test_dx[i] == y_pred_dx[i]:
                N += 1
            elif y_test_dx[i] == 0:
                L -= 1
        if L == 0 :
            L += 1
        pref_dx = float(N / L)
        pred_dxdf.append([save_path_dx, str(pref_dx)])
        #print(save_path_dx + ':' + str(pref_dx))

    out_pred_zk = out_pred_finish[(out_pred_finish['zk'] != 0)]
    out_pred_zk = out_pred_zk[-50:]
    y_test_zk_num = out_pred_zk['编号'].tolist()
    y_test_zk = []
    y_pred_zk = out_pred_zk['zk'].tolist()
    for i in y_test_zk_num:
        if int(out_finish.loc[out_finish['编号'] == int(i)]['zk_f']) == 1:
            y_test_zk.append('主')
        elif int(out_finish.loc[out_finish['编号'] == int(i)]['zk_f']) == -1:
            y_test_zk.append('客')
        else:# int(out_finish.loc[out_finish['编号'] == int(i)]['zk_f']) == 0:
            y_test_zk.append('走')
    L = len(y_test_zk)
    N = 0
    for i in range(L):
        if y_test_zk[i] == y_pred_zk[i]:
            N+=1
        elif y_test_zk[i] == '走':
            L-=1
    if L == 0:
        L += 1
    pref_zk = float(N / L)
    #print(pref_zk)
    pred_zkdf.append(['zk', str(pref_zk)])

    out_pred_dx = out_pred_finish[(out_pred_finish['dx'] != 0)]
    out_pred_dx = out_pred_dx[-50:]
    y_test_dx_num = out_pred_dx['编号'].tolist()
    y_test_dx = []
    y_pred_dx = out_pred_dx['dx'].tolist()
    for i in y_test_dx_num:
        if int(out_finish.loc[out_finish['编号'] == int(i)]['dx_f']) == 1:
            y_test_dx.append('大')
        elif int(out_finish.loc[out_finish['编号'] == int(i)]['dx_f']) == -1:
            y_test_dx.append('小')
        else:# int(out_finish.loc[out_finish['编号'] == int(i)]['zk_f']) == 0:
            y_test_dx.append('走')
    L = len(y_test_dx)
    N = 0
    for i in range(L):
        if y_test_dx[i] == y_pred_dx[i]:
            N += 1
        elif y_test_dx[i] == '走':
            L-=1
    if L == 0:
        L += 1
    pref_dx = float(N / L)
    #print(pref_dx)
    pred_dxdf.append(['dx', str(pref_dx)])
    pred_zkdf = pd.DataFrame(pred_zkdf)
    pred_dxdf = pd.DataFrame(pred_dxdf)
    print(pred_zkdf)
    print(pred_dxdf)

    curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    if (len(out_pred_1) >= 1):
        data_html = out_pred_1.to_html()
        predzk_html = pred_zkdf.to_html()
        preddx_html = pred_dxdf.to_html()
        send_html = predzk_html + preddx_html + data_html
        #print(send_html)
        ret = mail(send_html, curtime, 1)
    return

#forecast("CBA")