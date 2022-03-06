import urllib
import urllib.request
import re
import random
import time
import os
import organize
import numpy as np
import pandas as pd

close_time = 1200
alltimeflag = 0

user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64)", 'Mozilla/5.0 (Windows NT 6.3; WOW64)',
              'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
              'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
              'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
              'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
              'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
              'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
              'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50')

def HtoD(Udata):
    Udata.replace('平手', 0, inplace=True)
    Udata.replace('平手/半球', 0.25, inplace=True)
    Udata.replace('半球', 0.5, inplace=True)
    Udata.replace('半球/一球', 0.75, inplace=True)
    Udata.replace('一球', 1, inplace=True)
    Udata.replace('一球/球半', 1.25, inplace=True)
    Udata.replace('球半', 1.5, inplace=True)
    Udata.replace('球半/两球', 1.75, inplace=True)
    Udata.replace('两球', 2, inplace=True)
    Udata.replace('两球/两球半', 2.25, inplace=True)
    Udata.replace('两球半', 2.5, inplace=True)
    Udata.replace('两球半/三球', 2.75, inplace=True)
    Udata.replace('三球', 3, inplace=True)
    Udata.replace('三球/三球半', 3.25, inplace=True)
    Udata.replace('三球半', 3.5, inplace=True)
    Udata.replace('三球半/四球', 3.75, inplace=True)
    Udata.replace('四球', 4, inplace=True)
    Udata.replace('四球/四球半', 4.25, inplace=True)
    Udata.replace('四球半', 4.5, inplace=True)
    Udata.replace('四球半/五球', 4.75, inplace=True)
    Udata.replace('五球', 5, inplace=True)
    Udata.replace('五球/五球半', 5.25, inplace=True)
    Udata.replace('五球半', 5.5, inplace=True)
    Udata.replace('五球半/六球', 5.75, inplace=True)
    Udata.replace('六球', 6, inplace=True)
    Udata.replace('六球/六球半', 6.25, inplace=True)
    Udata.replace('六球半', 6.5, inplace=True)
    Udata.replace('六球半/七球', 6.75, inplace=True)
    Udata.replace('七球', 7, inplace=True)
    Udata.replace('七球/七球半', 7.25, inplace=True)
    Udata.replace('七球半', 7.5, inplace=True)
    Udata.replace('七球半/八球', 7.75, inplace=True)

    Udata.replace('受让平手/半球', -0.25, inplace=True)
    Udata.replace('受让半球', -0.5, inplace=True)
    Udata.replace('受让半球/一球', -0.75, inplace=True)
    Udata.replace('受让一球', -1, inplace=True)
    Udata.replace('受让一球/球半', -1.25, inplace=True)
    Udata.replace('受让球半', -1.5, inplace=True)
    Udata.replace('受让球半/两球', -1.75, inplace=True)
    Udata.replace('受让两球', -2, inplace=True)
    Udata.replace('受让两球/两球半', -2.25, inplace=True)
    Udata.replace('受让两球半', -2.5, inplace=True)
    Udata.replace('受让两球半/三球', -2.75, inplace=True)
    Udata.replace('受让三球', -3, inplace=True)
    Udata.replace('受让三球/三球半', -3.25, inplace=True)
    Udata.replace('受让三球半', -3.5, inplace=True)
    Udata.replace('受让三球半/四球', -3.75, inplace=True)
    Udata.replace('受让四球', -4, inplace=True)
    Udata.replace('受让四球/四球半', -4.25, inplace=True)
    Udata.replace('受让四球半', -4.5, inplace=True)
    Udata.replace('受让四球半/五球', -4.75, inplace=True)
    Udata.replace('受让五球', -5, inplace=True)
    Udata.replace('受让五球/五球半', -5.25, inplace=True)
    Udata.replace('受让五球半', -5.5, inplace=True)
    Udata.replace('受让五球半/六球', -5.75, inplace=True)
    Udata.replace('受让六球', -6, inplace=True)
    Udata.replace('受让六球/六球半', -6.25, inplace=True)
    Udata.replace('受让六球半', -6.5, inplace=True)
    Udata.replace('受让六球半/七球', -6.75, inplace=True)
    Udata.replace('受让七球', -7, inplace=True)
    Udata.replace('受让七球/七球半', -7.25, inplace=True)
    Udata.replace('受让七球半', -7.5, inplace=True)
    Udata.replace('受让七球半/八球', -7.75, inplace=True)

    Udata.replace('平手', 0, inplace = True)
    Udata.replace('平/半', 0.25, inplace = True)
    Udata.replace('半球', 0.5, inplace = True)
    Udata.replace('半/一', 0.75, inplace = True)
    Udata.replace('一球', 1, inplace = True)
    Udata.replace('一/球半', 1.25, inplace = True)
    Udata.replace('球半', 1.5, inplace = True)
    Udata.replace('球半/两', 1.75, inplace = True)
    Udata.replace('两球', 2, inplace = True)
    Udata.replace('两/两球半', 2.25, inplace = True)
    Udata.replace('两球半', 2.5, inplace = True)
    Udata.replace('两球半/三', 2.75, inplace = True)
    Udata.replace('三球', 3, inplace = True)
    Udata.replace('三/三球半', 3.25, inplace = True)
    Udata.replace('三球半', 3.5, inplace = True)
    Udata.replace('三球半/四', 3.75, inplace = True)
    Udata.replace('四球', 4, inplace = True)
    Udata.replace('四/四球半', 4.25, inplace=True)
    Udata.replace('四球半', 4.5, inplace=True)
    Udata.replace('四球半/五', 4.75, inplace=True)
    Udata.replace('五球', 5, inplace=True)
    Udata.replace('五/五球半', 5.25, inplace=True)
    Udata.replace('五球半', 5.5, inplace=True)
    Udata.replace('五球半/六', 5.75, inplace=True)
    Udata.replace('六球', 6, inplace=True)
    Udata.replace('六/六球半', 6.25, inplace=True)
    Udata.replace('六球半', 6.5, inplace=True)
    Udata.replace('六球半/七', 6.75, inplace=True)
    Udata.replace('七球', 7, inplace=True)
    Udata.replace('七/七球半', 7.25, inplace=True)
    Udata.replace('七球半', 7.5, inplace=True)
    Udata.replace('七球半/八', 7.75, inplace=True)

    Udata.replace('受平/半', -0.25, inplace = True)
    Udata.replace('受半球', -0.5, inplace = True)
    Udata.replace('受半/一', -0.75, inplace = True)
    Udata.replace('受一球', -1, inplace = True)
    Udata.replace('受一/球半', -1.25, inplace = True)
    Udata.replace('受球半', -1.5, inplace = True)
    Udata.replace('受球半/两', -1.75, inplace = True)
    Udata.replace('受两球', -2, inplace = True)
    Udata.replace('受两/两球半', -2.25, inplace = True)
    Udata.replace('受两球半', -2.5, inplace = True)
    Udata.replace('受两球半/三', -2.75, inplace = True)
    Udata.replace('受三球', -3, inplace = True)
    Udata.replace('受三/三球半', -3.25, inplace = True)
    Udata.replace('受三球半', -3.5, inplace = True)
    Udata.replace('受三球半/四', -3.75, inplace = True)
    Udata.replace('受四球', -4, inplace = True)
    Udata.replace('受四球/四球半', -4.25, inplace=True)
    Udata.replace('受四球半', -4.5, inplace=True)
    Udata.replace('受四球半/五', -4.75, inplace=True)
    Udata.replace('受五球', -5, inplace=True)
    Udata.replace('受五/五球半', -5.25, inplace=True)
    Udata.replace('受五球半', -5.5, inplace=True)
    Udata.replace('受五球半/六', -5.75, inplace=True)
    Udata.replace('受六球', -6, inplace=True)
    Udata.replace('受六/六球半', -6.25, inplace=True)
    Udata.replace('受六球半', -6.5, inplace=True)
    Udata.replace('受六球半/七', -6.75, inplace=True)
    Udata.replace('受七球', -7, inplace=True)
    Udata.replace('受七/七球半', -7.25, inplace=True)
    Udata.replace('受七球半', -7.5, inplace=True)
    Udata.replace('受七球半/八', -7.75, inplace=True)

    Udata.replace('0.5/1', 0.75, inplace=True)
    Udata.replace('1/1.5', 1.25, inplace=True)
    Udata.replace('1.5/2', 1.75, inplace=True)
    Udata.replace('2/2.5', 2.25, inplace=True)
    Udata.replace('2.5/3', 2.75, inplace=True)
    Udata.replace('3/3.5', 3.25, inplace=True)
    Udata.replace('3.5/4', 3.75, inplace=True)
    Udata.replace('4/4.5', 4.25, inplace=True)
    Udata.replace('4.5/5', 4.75, inplace=True)
    Udata.replace('5/5.5', 5.25, inplace=True)
    Udata.replace('5.5/6', 5.75, inplace=True)
    Udata.replace('6/6.5', 6.25, inplace=True)
    Udata.replace('6.5/7', 6.75, inplace=True)
    Udata.replace('7/7.5', 7.25, inplace=True)
    Udata.replace('7.5/8', 7.75, inplace=True)
    Udata.replace('8/8.5', 8.25, inplace=True)
    Udata.replace('8.5/9', 8.75, inplace=True)

    return Udata

def spider( Lname ):
    stock_total = [] #stock_total：所有页面的数据
    if Lname == 'NBA':
        url = 'http://guess2.win007.com/basket/'
        pattern_str = '(?<=zt_)(\d*)'
    elif Lname == 'CBA':
        url = 'http://guess2.win007.com/basket/'
        pattern_str = '(?<=zt_)(\d*)'
    elif Lname == 'FOOTBALL':
        url = 'http://guess2.win007.com/'
        pattern_str = '(?<=id=\'time_)(\d*)'
    #url = 'http://guess2.win007.com/'
    # request=urllib.request.Request(url=url,headers={"User-Agent":random.choice(user_agent)})#随机从user_agent列表中抽取一个元素
    # response=urllib.request.urlopen(request,timeout=5)
    # content=response.read().decode('UTF-8')       #读取网页内容
    content = grabs(url)
    if content == 0 :
        return
    time.sleep(random.randrange(1, 2))
    pattern = re.compile(pattern_str)
    game_id = re.findall(pattern, str(content))  # 正则匹配
    print(game_id)
    return game_id

def grabs (url):
    user_agent_used = []
    user_agent_used = list(user_agent)
    attempts = 0
    success = False
    while attempts < 10 and not success:
        # print(attempts)
        try:
            #url = 'http://vip.win007.com/AsianOdds_n.aspx?id=' + str(gameid) + '&l=0'
            user_agent_use = random.choice(user_agent_used)
            user_agent_used.remove(user_agent_use)
            # print(user_agent_use)
            request = urllib.request.Request(url=url, headers={"User-Agent": user_agent_use})  # 随机从user_agent列表中抽取一个元素
            response = urllib.request.urlopen(request, timeout=10)
            content = response.read().decode('UTF-8')  # 读取网页内容
            time.sleep(random.random())#randrange(1, 2)
            success = True
        except:
            attempts += 1
            if attempts == 10:
                break
    # print(content)
    if attempts == 10:
        return 0
    return content


def footballspider(gameid):
    root = os.getcwd() # 获取当前路径
    stock_total=[]   #stock_total：所有页面的数据
    #gameid = 1910700
    #for page in range(1,2):
    # url = 'http://vip.win007.com/AsianOdds_n.aspx?id=' + str(gameid) + '&l=0'
    # user_agent_used = []
    # user_agent_used = list(user_agent)
    # user_agent_use = random.choice(user_agent_used)
    # user_agent_used.remove(user_agent_use)
    # print(user_agent_use)
    # request = urllib.request.Request(url=url,headers={"User-Agent": user_agent_use})  # 随机从user_agent列表中抽取一个元素
    # response = urllib.request.urlopen(request,timeout=10)
    # content = response.read().decode('UTF-8')  # 读取网页内容
    # time.sleep(random.randrange(1, 2))
    # user_agent_used = []
    # user_agent_used = list(user_agent)
    # attempts = 0
    # success = False
    # while attempts < 10 and not success:
    #     #print(attempts)
    #     try:
    #         url = 'http://vip.win007.com/AsianOdds_n.aspx?id=' + str(gameid) + '&l=0'
    #         user_agent_use = random.choice(user_agent_used)
    #         user_agent_used.remove(user_agent_use)
    #         #print(user_agent_use)
    #         request = urllib.request.Request(url=url, headers={"User-Agent": user_agent_use})  # 随机从user_agent列表中抽取一个元素
    #         response = urllib.request.urlopen(request, timeout=10)
    #         content = response.read().decode('UTF-8')  # 读取网页内容
    #         time.sleep(random.randrange(1, 2))
    #         success = True
    #     except:
    #         attempts += 1
    #         if attempts == 10:
    #             break
    # # print(content)
    # if attempts == 10:
    #     return
    url = 'http://vip.win007.com/AsianOdds_n.aspx?id=' + str(gameid) + '&l=0'
    content = grabs(url)
    if content == 0:
        return
    pattern = re.compile('(?<= alt=")([\s\S].*?)\" t')
    team_name = re.findall(pattern, str(content))
    team_name[0] = str(team_name[0]).replace(" ", "")
    team_name[1] = str(team_name[1]).replace(" ", "")
    print(team_name)

    content1 = str(content).replace(" ", "").replace("\r", "").replace("\n", "")
    #print(content1)
    pattern = re.compile('(?<=id="headVs">)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)')
    VS = re.findall(pattern, str(content1))
    if(len(VS) == 0):
        pattern = re.compile('(?<=="rowredb">)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)')
        VS = re.findall(pattern, str(content1))
        if(len(VS) == 0):
            pattern = re.compile('(?<=class=\'vs\'>)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)')
            VS = re.findall(pattern, str(content1))
    print(VS)

    if (VS[0] == '推迟'):
        organize.spider_delay(gameid,"FOOTBALL")
        return

    pattern = re.compile('(?<=class="LName">)\S+')#(?=<)
    LName = re.findall(pattern, str(content))
    print(LName)
    Lname = str(LName[0])
    print(Lname)
    # if((Lname != 'NBA') & (Lname != 'CBA')):
    #     spider_done(gameid)
    #     return

    pattern = re.compile('(?<=\t)[0-9]*|\d{4}-\d{2}-\d{2} \d{2}:\d{2}(?=\&)')
    playtime = re.findall(pattern, str(content))
    print(playtime)

    for i in playtime:
        if i == '':
            playtime.remove(i)
    time_now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    time_diff = time.mktime(time.strptime(str(playtime[0]), "%Y-%m-%d %H:%M")) - time.mktime(
        time.strptime(str(time_now), "%Y-%m-%d %H:%M"))
    #print(time_now)
    #print(time_diff)
    if alltimeflag == 0:
        if ((time_diff < close_time)):#(time_diff > -close_time)&
            print('1 hours in')
            if (time_diff < -close_time):
                if (VS[0] != '完'):
                    print('未完赛')
                    return
        else:
            print('1 hours out')
            return
    else:
        if ((time_diff < 86400)):#(time_diff > -86400*2)&
            print('24 hours in')
        else:
            print('24 hours out')
            return


    pattern = re.compile('(?<=<div class="score">)(\d*)')
    score = re.findall(pattern, str(content))
    if(len(score) == 0):
        score = ['0', '0']
    else:
        for i in range(len(score)):
            if score[i] == '':
                score[i] = '0'

    print(score)

    pattern = re.compile('(?<=id="odds")[\s\S]+<div id="MiddleAd"')
    tbody = re.findall(pattern, str(content))
    #print(tbody)

    tbody = str(tbody).replace(" ", "").replace("\\r", "").replace("\\n", "")
    #tbody = str(tbody).replace("\\r", "")
    #tbody = str(tbody).replace("\\n", "")
    #print(tbody)
    pattern = re.compile('(?<=>)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)|(?<=home_)[0-9]*|\d{4}-\d{2}-\d{2} \d{2}:\d{2}')
    state = re.findall(pattern, str(tbody))
    #print(state)
    a = ['初', '多盘口', '即时', '终', '历史资料', '详', '主', '客', '同', '公司', '主队', '盘口', '客队', '统', '最大值', '最小值', '标注', '取消', '-']
    company = ['澳门', '易胜博', 'Crown', '365', '韦德', '威廉', 'Interwetten', '立博', '12B', '利记', '盈禾', '10B', '明陞', '金宝博',
               '18B', '平博', '香港马会' ,'盘口2','盘口3','盘口4','盘口5']
    company_major = ['易胜博', 'Crown', '365', '韦德', '明陞', '12B', '10B', '18B', '金宝博', '利记', '盈禾', '平博']
    black_list = ['0', '0', '0', '0', '0', '0', '0', '0', '0']

    for i in a:
        while i in state:
            state.remove(i)
    #print(state)
    for i in range(len(state)-1,-1,-1):
        if state[i] in company:
            # print('ture')
            if (i >= (len(state) - 9)):
                for j in black_list:
                    state.insert(i + 1, j)
            for k in range(len(black_list)):
                #print(state)
                if (state[i + k + 1] in company):
                    state.insert(i + k + 1, black_list[k])

    #print(state)
    result = []  # result：最终数据
    Hang = (int)(len(state)/10)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 10):
            if x == 0:
                result.append([])
            result[y].append(state[x + y * 10])
    #print(result)
    result_df = pd.DataFrame(result)
    #print(result_df)
    result_df = result_df.drop([4, 5, 6], axis=1)
    for i in company:
        if i not in company_major:
            result_df = result_df[result_df[0] != i]


    # result_df = result_df[result_df[0] != '盘口2']
    # result_df = result_df[result_df[0] != '盘口3']
    # result_df = result_df[result_df[0] != '盘口4']
    # result_df = result_df[result_df[0] != '盘口5']
    result_df = HtoD(result_df)
    #print(result_df)
    # if (float(score[0]) - float(score[1]) > float(result1[i + 2])):
    result1 = np.array(result_df)
    #print(result1)
    result1 = result1.flatten()
    result1 = result1.tolist()
    #print(result1)
    # Hang = (int)(len(result1) / 7)
    # for i in range(len(result1)+Hang*2):
    #     if result1[i] in company:
    #         if (float(score[0]) - float(score[1]) > float(result1[i + 2])):
    #             result1.insert(i + 1, '1')
    #         elif (float(score[0]) - float(score[1]) == float(result1[i + 2])):
    #             result1.insert(i + 1, '0')
    #         elif (float(score[0]) - float(score[1]) < float(result1[i + 2])):
    #             result1.insert(i + 1, '-1')
    #
    #         if (float(score[0]) - float(score[1]) > float(result1[i + 6])):
    #             result1.insert(i + 2, '1')
    #         elif (float(score[0]) - float(score[1]) == float(result1[i + 6])):
    #             result1.insert(i + 2, '0')
    #         elif (float(score[0]) - float(score[1]) < float(result1[i + 6])):
    #             result1.insert(i + 2, '-1')
    #print(result1)

    # url = 'http://vip.win007.com/OverDown_n.aspx?id=' + str(gameid) +'&l=0'
    # user_agent_use = random.choice(user_agent_used)
    # user_agent_used.remove(user_agent_use)
    # print(user_agent_use)
    # request = urllib.request.Request(url=url,headers={"User-Agent": user_agent_use})  # 随机从user_agent列表中抽取一个元素
    # response = urllib.request.urlopen(request,timeout=10)
    # content = response.read().decode('UTF-8')  # 读取网页内容
    # time.sleep(random.randrange(1, 2))

    # attempts = 0
    # success = False
    # while attempts < 5 and not success:
    #     #print(attempts)
    #     try:
    #         url = 'http://vip.win007.com/OverDown_n.aspx?id=' + str(gameid) + '&l=0'
    #         user_agent_use = random.choice(user_agent_used)
    #         user_agent_used.remove(user_agent_use)
    #         #print(user_agent_use)
    #         request = urllib.request.Request(url=url, headers={"User-Agent": user_agent_use})  # 随机从user_agent列表中抽取一个元素
    #         response = urllib.request.urlopen(request, timeout=10)
    #         content = response.read().decode('UTF-8')  # 读取网页内容
    #         time.sleep(random.randrange(1, 2))
    #         success = True
    #     except:
    #         attempts += 1
    #         if attempts == 5:
    #             break
    url = 'http://vip.win007.com/OverDown_n.aspx?id=' + str(gameid) + '&l=0'
    content = grabs(url)
    if content == 0:
        return
    pattern = re.compile('(?<=id="odds")[\s\S]+最大值')
    tbody = re.findall(pattern, str(content))
    #print(tbody)

    tbody = str(tbody).replace(" ", "")
    tbody = str(tbody).replace("\\r", "")
    tbody = str(tbody).replace("\\n", "")
    #print(tbody)
    pattern = re.compile(
        '(?<=>)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)|(?<=home_)[0-9]*|\d{4}-\d{2}-\d{2} \d{2}:\d{2}')
    state = re.findall(pattern, str(tbody))
    #print(state)
    a = ['初', '多盘口', '即时', '终', '历史资料', '变化时间', '详', '主', '客', '同', '公司', '大球', '进球数', '小球', '统', '最大值', '最小值', '标注', '取消', '-']
    for i in a:
        while i in state:
            state.remove(i)
    #print(state)
    # for i in range(len(state)-1,-1,-1):
    #     if state[i] in company:
    #         # print('ture')
    #         if (i >= (len(state) - 9)):
    #             for j in black_list:
    #                 state.insert(i + 1, j)
    #         for kk in range(len(black_list)):
    #             if (state[i + j + 1] in company):
    #                 state.insert(i + k + 1, black_list[k])
    #         # elif (state[i + 1] in company):
    #         #     for j in black_list:
    #         #         state.insert(i+1, j)
    #
    for i in range(len(state)-1,-1,-1):
        if state[i] in company:
            # print('ture')
            if (i >= (len(state) - 9)):
                for j in black_list:
                    state.insert(i + 1, j)
            for k in range(len(black_list)):
                #print(state)
                if (state[i + k + 1] in company):
                    state.insert(i + k + 1, black_list[k])

    result = []  # result：最终数据
    Hang = (int)(len(state)/10)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 10):
            if x == 0:
                result.append([])
            result[y].append(state[x + y * 10])
    #print(result)
    result_df = pd.DataFrame(result)
    result_df = result_df.drop([4, 5, 6], axis=1)
    for i in company:
        if i not in company_major:
            result_df = result_df[result_df[0] != i]
    # result_df = result_df[result_df[0] != '盘口2']
    # result_df = result_df[result_df[0] != '盘口3']
    # result_df = result_df[result_df[0] != '盘口4']
    # result_df = result_df[result_df[0] != '盘口5']
    #result_df = result_df.drop(result_df[result_df[0]=='盘口2'],axis=0)
    result_df = HtoD(result_df)
    #print(result_df)
    result2 = np.array(result_df)
    result2 = result2.flatten()
    result2 = result2.tolist()
    #print(result2)
    # Hang = (int)(len(result2) / 7)
    # for i in range(len(result2)+Hang*2):
    #     if result2[i] in company:
    #         if (float(score[0]) + float(score[1]) > float(result2[i + 2])):
    #             result2.insert(i + 1, '1')
    #         elif (float(score[0]) + float(score[1]) == float(result2[i + 2])):
    #             result2.insert(i + 1, '0')
    #         elif (float(score[0]) + float(score[1]) < float(result2[i + 2])):
    #             result2.insert(i + 1, '-1')
    #
    #         if (float(score[0]) + float(score[1]) > float(result2[i + 6])):
    #             result2.insert(i + 2, '1')
    #         elif (float(score[0]) + float(score[1]) == float(result2[i + 6])):
    #             result2.insert(i + 2, '0')
    #         elif (float(score[0]) + float(score[1]) < float(result2[i + 6])):
    #             result2.insert(i + 2, '-1')
    #print(result2)
    #url = 'http://zq.win007.com/analysis/'+str(gameid)+'.htm'
    url_list = ['http://zq.win007.com/analysis/' + str(gameid) + '.htm',
                'http://zq.win007.com/analysis/' + str(gameid) + 'cn.htm',
                'http://zq.win007.com/analysis/' + str(gameid) + 'sb.htm',
                'http://info.win007.com/analysis/' + str(gameid) + '.htm',
                'http://info.win007.com/analysis/' + str(gameid) + 'cn.htm',
                'http://info.win007.com/analysis/' + str(gameid) + 'sb.htm']
    # attempts = 0
    # success = False
    # while attempts < 5 and not success:
    #     #print(attempts)
    #     try:
    #         url = random.choice(url_list)
    #         user_agent_use = random.choice(user_agent_used)
    #         user_agent_used.remove(user_agent_use)
    #         #print(user_agent_use)
    #         request = urllib.request.Request(url=url, headers={"User-Agent": user_agent_use})  # 随机从user_agent列表中抽取一个元素
    #         response = urllib.request.urlopen(request, timeout=10)
    #         content = response.read().decode('UTF-8')  # 读取网页内容
    #         time.sleep(random.randrange(1, 2))
    #         success = True
    #     except:
    #         attempts += 1
    #         if attempts == 5:
    #             break
    url = random.choice(url_list)
    content = grabs(url)
    if content == 0:
        return

    pattern = re.compile('(?<=var h_data)[\S\s]+(?=var a_data)')
    state = re.findall(pattern, str(content))
    #print(state)
    state = str(state)
    state = state.replace('\'', '').replace('[', '').replace(']', '').replace(';', '').replace(' ', '').replace('\\r', '').replace('\\n', '')
    state = state.split(',')
    #print(state)
    e_data = []  # result：最终数据

    Hang = (int)(len(state) / 20)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 20):
            if x == 0:
                e_data.append([])
            e_data[y].append(state[x + y * 20])

    data = e_data
    Win_5 = 0
    Win_10 = 0
    Handicap_5 = 0
    Handicap_10 = 0
    Big_5 = 0
    Big_10 = 0

    for i in range(Hang):
        if i < 5:
            if (int(data[i][12]) == 1):
                Win_5 += 1
            if (int(data[i][13]) == 1):
                Handicap_5 += 1
            if (int(data[i][14]) == 1):
                Big_5 += 1
        if i < 10:
            if (int(data[i][12]) == 1):
                Win_10 += 1
            if (int(data[i][13]) == 1):
                Handicap_10 += 1
            if (int(data[i][14]) == 1):
                Big_10 += 1

    e_Win_5 = round(float(Win_5 / 5), 2)
    e_Handicap_5 = round(float(Handicap_5 / 5), 2)
    e_Big_5 = round(float(Big_5 / 5), 2)
    e_Win_10 = round(float(Win_10 / 10), 2)
    e_Handicap_10 = round(float(Handicap_10 / 10), 2)
    e_Big_10 = round(float(Big_10 / 10), 2)
    # print(e_Win_5)
    # print(e_Handicap_5)
    # print(e_Big_5)
    # print(e_Win_10)
    # print(e_Handicap_10)
    # print(e_Big_10)

    pattern = re.compile('(?<=var a_data)[\S\s]+(?=var h2_data)')
    state = re.findall(pattern, str(content))
    #print(state)
    state = str(state)
    state = state.replace('\'', '').replace('[', '').replace(']', '').replace(';', '').replace(' ', '').replace('\\r','').replace('\\n', '')
    state = state.split(',')
    #print(state)
    f_data = []  # result：最终数据

    Hang = (int)(len(state) / 20)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 20):
            if x == 0:
                f_data.append([])
            f_data[y].append(state[x + y * 20])

    data = f_data
    Win_5 = 0
    Win_10 = 0
    Handicap_5 = 0
    Handicap_10 = 0
    Big_5 = 0
    Big_10 = 0

    for i in range(Hang):
        if i < 5:
            if (int(data[i][12]) == 1):
                Win_5 += 1
            if (int(data[i][13]) == 1):
                Handicap_5 += 1
            if (int(data[i][14]) == 1):
                Big_5 += 1
        if i < 10:
            if (int(data[i][12]) == 1):
                Win_10 += 1
            if (int(data[i][13]) == 1):
                Handicap_10 += 1
            if (int(data[i][14]) == 1):
                Big_10 += 1

    f_Win_5 = round(float(Win_5 / 5), 2)
    f_Handicap_5 = round(float(Handicap_5 / 5), 2)
    f_Big_5 = round(float(Big_5 / 5), 2)
    f_Win_10 = round(float(Win_10 / 10), 2)
    f_Handicap_10 = round(float(Handicap_10 / 10), 2)
    f_Big_10 = round(float(Big_10 / 10), 2)
    # print(f_Win_5)
    # print(f_Handicap_5)
    # print(f_Big_5)
    # print(f_Win_10)
    # print(f_Handicap_10)
    # print(f_Big_10)
    '''
    pattern = re.compile(
        '(?<=var h_ranking=)[\S\s]+(?=var g_ranking)')
    state = re.findall(pattern, str(content))
    state = str(state)
    state = state.replace('\'', '').replace('[', '').replace(']', '').replace(';', '').replace(' ', '').replace('\\r', '').replace('\\n', '').replace('\"', '')
    Hrank = state.split(',')
    #print(state)
    pattern = re.compile(
        '(?<=var g_ranking=)[\S\s]+(?=var v_data)')
    state = re.findall(pattern, str(content))
    state = str(state)
    state = state.replace('\'', '').replace('[', '').replace(']', '').replace(';', '').replace(' ', '').replace('\\r', '').replace('\\n', '').replace('\"', '')
    Grank = state.split(',')
    #print(state)

    ranking = [e_AveG, e_AveL, e_AveHG, e_AveHL, e_AveGG, e_AveGL, e_AveG5, e_AveL5, e_AveG10, e_AveL10] + Hrank + [f_AveG, f_AveL, f_AveHG, f_AveHL, f_AveGG, f_AveGL, f_AveG5, f_AveL5, f_AveG10, f_AveL10] + Grank
    #print(ranking)
    '''
    probability = [e_Win_5, e_Handicap_5, e_Big_5, e_Win_10, e_Handicap_10, e_Big_10, f_Win_5, f_Handicap_5, f_Big_5, f_Win_10, f_Handicap_10, f_Big_10]
    gameid_list = [gameid]

    result =  gameid_list + playtime + LName + team_name + VS + score + probability + result1 + result2

    if (float(score[0]) - float(score[1]) > float(result1[5])):
        result.insert(8, '1')
    elif (float(score[0]) - float(score[1]) == float(result1[5])):
        result.insert(8, '0')
    elif (float(score[0]) - float(score[1]) < float(result1[5])):
        result.insert(8, '-1')

    if (float(score[0]) - float(score[1]) > float(result1[5])):
        result.insert(9, '1')
    elif (float(score[0]) - float(score[1]) == float(result1[5])):
        result.insert(9, '0')
    elif (float(score[0]) - float(score[1]) < float(result1[5])):
        result.insert(9, '-1')

    if (float(score[0]) + float(score[1]) > float(result2[5])):
        result.insert(10, '1')
    elif (float(score[0]) + float(score[1]) == float(result2[5])):
        result.insert(10, '0')
    elif (float(score[0]) + float(score[1]) < float(result2[5])):
        result.insert(10, '-1')

    if (float(score[0]) + float(score[1]) > float(result2[5])):
        result.insert(11, '1')
    elif (float(score[0]) + float(score[1]) == float(result2[5])):
        result.insert(11, '0')
    elif (float(score[0]) + float(score[1]) < float(result2[5])):
        result.insert(11, '-1')


    # result = np.array(result)
    # result = result.transpose()
    # print(result)

    result_df = pd.DataFrame(result)#, columns=['编号', '时间', '联赛', '主队', '客队', '联赛', '公司1', '初主', '初盘', '初客', '终主', '终盘', '终客', '公司2', '初主', '初盘', '初客', '终主', '终盘', '终客', '公司3', '初主', '初盘', '初客', '终主', '终盘', '终客', '公司4', '初主', '初盘', '初客', '终主', '终盘', '终客', '公司5', '初主', '初盘', '初客', '终主', '终盘', '终客', '公司6', '初主', '初盘', '初客', '终主', '终盘', '终客'])
    result_df = result_df.transpose()
    path = root + '/' + 'Fdata' + '.xlsx'

    if (os.path.isfile(path)):
        Fdata = pd.read_excel(path)
        result_df = Fdata.append(result_df, ignore_index=True)
    result_df[0] = result_df[0].astype('str')

    result_df = result_df.drop_duplicates(subset=[0], keep='last')
    result_df.sort_values(1, inplace=True)
    result_df.to_excel(path, index=None)

    if (VS[0] == '完'):
        organize.spider_done(gameid,"FOOTBALL")
        return
    return


def basketballspider(gameid):
    root = os.getcwd() # 获取当前路径
    stock_total=[]   #stock_total：所有页面的数据

    url = 'http://nba.win007.com/odds/AsianOdds_n.aspx?id=' + str(gameid)
    content = grabs(url)
    if content == 0:
        return
    pattern = re.compile('(?<= alt=")([\s\S].*?)\" t')
    team_name = re.findall(pattern, str(content))
    print(team_name)

    content1 = str(content).replace(" ", "").replace("\r", "").replace("\n", "")
    #print(content1)
    pattern = re.compile('(?<=id="headVs">)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)')
    VS = re.findall(pattern, str(content1))
    if(len(VS) == 0):
        pattern = re.compile('(?<=="rowredb">)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)')
        VS = re.findall(pattern, str(content1))
        if(len(VS) == 0):
            pattern = re.compile('(?<=class=\'vs\'>)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)')
            VS = re.findall(pattern, str(content1))
    print(VS)

    if (VS[0] == '推迟'):
        organize.spider_delay(gameid, "NBA")
        return

    pattern = re.compile('(?<=class="LName">)\S+(?=<)')
    LName = re.findall(pattern, str(content))
    print(LName)
    Lname = str(LName[0])
    print(Lname)
    if((Lname != 'NBA') & (Lname != 'CBA')):
        organize.spider_done(gameid,'NBA')
        return

    pattern = re.compile('(?<=\t)[0-9]*|\d{4}-\d{2}-\d{2} \d{2}:\d{2}(?=\&)')
    playtime = re.findall(pattern, str(content))
    print(playtime)

    for i in playtime:
        if i == '':
            playtime.remove(i)
    time_now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    time_diff = time.mktime(time.strptime(str(playtime[0]), "%Y-%m-%d %H:%M")) - time.mktime(
        time.strptime(str(time_now), "%Y-%m-%d %H:%M"))
    # print(playtime[0])
    # print(time_now)
    # print(time_diff)

    # if ((time_diff < 2400)):#(time_diff >- 2400)&
    #     print('1 hours in')
    # else:
    #     print('1 hours out')
    #     return

    # if ((time_diff < 86400)):
    #     print('24 hours in')
    # else:
    #     print('24 hours out')
    #     return

    if alltimeflag == 0:
        if ((time_diff < close_time)):#(time_diff > -close_time)&
            print('1 hours in')
            if(time_diff < -close_time):
                if (VS[0] != '完'):
                    print('未完赛')
                    return
        else:
            print('1 hours out')
            return
    else:
        if ((time_diff < 86400)):#(time_diff > -86400*2)&
            print('24 hours in')
        else:
            print('24 hours out')
            return

    pattern = re.compile('(?<=<div class="score">)(\d*)')
    score = re.findall(pattern, str(content))
    if(len(score) == 0):
        score = ['0', '0']
    print(score)

    pattern = re.compile('(?<=id="odds")[\s\S]+<div id="MiddleAd"')
    tbody = re.findall(pattern, str(content))
    #print(tbody)

    tbody = str(tbody).replace(" ", "").replace("\\r", "").replace("\\n", "")
    #tbody = str(tbody).replace("\\r", "")
    #tbody = str(tbody).replace("\\n", "")
    #print(tbody)
    pattern = re.compile('(?<=>)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)|(?<=home_)[0-9]*|\d{4}-\d{2}-\d{2} \d{2}:\d{2}')
    state = re.findall(pattern, str(tbody))
    #print(state)
    a = ['初', '多盘口', '即', '终', '历史资料', '详', '主', '客', '同', '公司', '主队', '盘口', '客队']
    company = ['澳门', '易胜博', 'Crown', '365', '韦德', '威廉', 'Interwetten', '立博', '12B', '利记']
    black_list = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
    for i in a:
        while i in state:
            state.remove(i)
    #print(state)
    for i in range(len(state)-1,-1,-1):
        if state[i] in company:
            # print('ture')
            if (i == (len(state) - 1)):
                for j in black_list:
                    state.insert(i + 1, j)
            elif (state[i + 1] in company):
                for j in black_list:
                    state.insert(i+1, j)

    #print(state)
    result = []  # result：最终数据
    Hang = (int)(len(state)/10)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 10):
            if x == 0:
                result.append([])
            result[y].append(state[x + y * 10])
    #print(result)
    result_df = pd.DataFrame(result)
    result_df = result_df.drop([4, 5, 6], axis=1)
    result_df = result_df[result_df[0] != '盘口2']
    result_df = result_df[result_df[0] != '盘口3']
    result_df = result_df[result_df[0] != '盘口4']
    result_df = result_df[result_df[0] != '盘口5']
    #print(result_df)
    result1 = np.array(result_df)
    #print(result1)
    result1 = result1.flatten()
    result1 = result1.tolist()
    # Hang = (int)(len(result1) / 7)
    # for i in range(len(result1)+Hang*2):
    #     if result1[i] in company:
    #         if (float(score[0]) - float(score[1]) > float(result1[i + 2])):
    #             result1.insert(i + 1, '1')
    #         elif (float(score[0]) - float(score[1]) == float(result1[i + 2])):
    #             result1.insert(i + 1, '0')
    #         elif (float(score[0]) - float(score[1]) < float(result1[i + 2])):
    #             result1.insert(i + 1, '-1')
    #
    #         if (float(score[0]) - float(score[1]) > float(result1[i + 6])):
    #             result1.insert(i + 2, '1')
    #         elif (float(score[0]) - float(score[1]) == float(result1[i + 6])):
    #             result1.insert(i + 2, '0')
    #         elif (float(score[0]) - float(score[1]) < float(result1[i + 6])):
    #             result1.insert(i + 2, '-1')
    # print(result1)

    url = 'https://nba.win007.com/odds/OverDown_n.aspx?id=' + str(gameid) + '&l=0'
    content = grabs(url)
    if content == 0:
        return
    #pattern = re.compile('(?<= alt=")([\s\S].*?)\" t')
    #team_name = re.findall(pattern, str(content))
    #print(team_name)

    pattern = re.compile('(?<=id="odds")[\s\S]+<div id="MiddleAd"')
    tbody = re.findall(pattern, str(content))
    #print(tbody)

    tbody = str(tbody).replace(" ", "")
    tbody = str(tbody).replace("\\r", "")
    tbody = str(tbody).replace("\\n", "")
    #print(tbody)
    pattern = re.compile(
        '(?<=>)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)|(?<=home_)[0-9]*|\d{4}-\d{2}-\d{2} \d{2}:\d{2}')
    state = re.findall(pattern, str(tbody))
    #print(state)
    a = ['初', '多盘口', '即', '终', '变化时间', '详', '主', '客', '同', '公司', '大分', '盘口', '小分']
    for i in a:
        while i in state:
            state.remove(i)
    #print(state)
    for i in range(len(state)-1,-1,-1):
        if state[i] in company:
            # print('ture')
            if (i == (len(state) - 1)):
                for j in black_list:
                    state.insert(i + 1, j)
            elif (state[i + 1] in company):
                for j in black_list:
                    state.insert(i+1, j)

    result = []  # result：最终数据
    Hang = (int)(len(state)/10)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 10):
            if x == 0:
                result.append([])
            result[y].append(state[x + y * 10])
    #print(result)
    result_df = pd.DataFrame(result)
    result_df = result_df.drop([4, 5, 6], axis=1)
    result_df = result_df[result_df[0] != '盘口2']
    result_df = result_df[result_df[0] != '盘口3']
    result_df = result_df[result_df[0] != '盘口4']
    result_df = result_df[result_df[0] != '盘口5']
    #result_df = result_df.drop(result_df[result_df[0]=='盘口2'],axis=0)
    #print(result_df)
    result2 = np.array(result_df)
    result2 = result2.flatten()
    result2 = result2.tolist()
    #print(result2)
    # Hang = (int)(len(result2) / 7)
    # for i in range(len(result2)+Hang*2):
    #     if result2[i] in company:
    #         if (float(score[0]) + float(score[1]) > float(result2[i + 2])):
    #             result2.insert(i + 1, '1')
    #         elif (float(score[0]) + float(score[1]) == float(result2[i + 2])):
    #             result2.insert(i + 1, '0')
    #         elif (float(score[0]) + float(score[1]) < float(result2[i + 2])):
    #             result2.insert(i + 1, '-1')
    #
    #         if (float(score[0]) + float(score[1]) > float(result2[i + 6])):
    #             result2.insert(i + 2, '1')
    #         elif (float(score[0]) + float(score[1]) == float(result2[i + 6])):
    #             result2.insert(i + 2, '0')
    #         elif (float(score[0]) + float(score[1]) < float(result2[i + 6])):
    #             result2.insert(i + 2, '-1')
    # print(result2)
    url = 'http://nba.win007.com/analysis/'+str(gameid)+'.htm'
    content = grabs(url)
    if content == 0:
        return
    #print(content)
    pattern = re.compile(
        '(?<=var e_data=)[\S\s]+(?=var f_data)')
    state = re.findall(pattern, str(content))
    state = str(state)
    state = state.replace('\'', '').replace('[', '').replace(']', '').replace(';', '').replace(' ', '').replace('\\r', '').replace('\\n', '')
    state = state.split(',')
    e_data = []  # result：最终数据
    Hang = (int)(len(state) / 27)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 27):
            if x == 0:
                e_data.append([])
            e_data[y].append(state[x + y * 27])
    #print(e_data)

    data = e_data
    Get = 0
    Lose = 0
    Hcount = 0
    Gcount = 0
    H_Get = 0
    H_Lose = 0
    G_Get = 0
    G_Lose = 0
    Get_5 = 0
    Lose_5 = 0
    Get_10 = 0
    Lose_10 = 0
    for i in range(Hang):
        Get += int(data[i][3])
        Lose += int(data[i][4])
        if i < 5 :
            Get_5 += int(data[i][3])
            Lose_5 += int(data[i][4])
        if i<10:
            Get_10 += int(data[i][3])
            Lose_10 += int(data[i][4])
        if(int(data[i][5]) == 1):
            Hcount += 1
            H_Get += int(data[i][3])
            H_Lose += int(data[i][4])
        elif(int(data[i][5]) == 0):
            Gcount += 1
            G_Get += int(data[i][3])
            G_Lose += int(data[i][4])

    e_AveG = round(float(Get / Hang),2)
    e_AveL = round(float(Lose / Hang),2)
    e_AveHG = round(float(H_Get / Hcount),2)
    e_AveHL = round(float(H_Lose / Hcount),2)
    e_AveGG = round(float(G_Get / Gcount),2)
    e_AveGL = round(float(G_Lose / Gcount),2)
    e_AveG5 = round(float(Get_5 / 5), 2)
    e_AveL5 = round(float(Lose_5 / 5), 2)
    e_AveG10 = round(float(Get_10 / 10), 2)
    e_AveL10 = round(float(Lose_10 / 10), 2)

    pattern = re.compile(
        '(?<=var h_data=)[\S\s]+(?=var a_data)')
    state = re.findall(pattern, str(content))
    state = str(state)
    state = state.replace('\'', '').replace('[', '').replace(']', '').replace(';', '').replace(' ', '').replace('\\r',
                                                                                                                '').replace(
        '\\n', '')
    state = state.split(',')
    v_data = []  # result：最终数据
    Hang = (int)(len(state) / 36)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 36):
            if x == 0:
                v_data.append([])
            v_data[y].append(state[x + y * 36])
    # v_data_df = pd.DataFrame(v_data)
    # pd.set_option('display.max_columns', None)
    # print(v_data_df)
    data = v_data
    Win_5 = 0
    Win_10 = 0
    Handicap_5 = 0
    Handicap_10 = 0
    Big_5 = 0
    Big_10 = 0

    for i in range(Hang):
        if i < 5:
            if ((data[i][9]) == '1'):
                Win_5 += 1
            if ((data[i][12]) == '1'):
                Handicap_5 += 1
            if ((data[i][15]) == '1'):
                Big_5 += 1
        if i < 10:
            if ((data[i][9]) == '1'):
                Win_10 += 1
            if ((data[i][12]) == '1'):
                Handicap_10 += 1
            if ((data[i][15]) == '1'):
                Big_10 += 1

    e_Win_5 = round(float(Win_5 / 5), 2)
    e_Handicap_5 = round(float(Handicap_5 / 5), 2)
    e_Big_5 = round(float(Big_5 / 5), 2)
    e_Win_10 = round(float(Win_10 / 10), 2)
    e_Handicap_10 = round(float(Handicap_10 / 10), 2)
    e_Big_10 = round(float(Big_10 / 10), 2)

    pattern = re.compile(
        '(?<=var f_data=)[\S\s]+(?=var h_ranking)')
    state = re.findall(pattern, str(content))
    state = str(state)
    state = state.replace('\'', '').replace('[', '').replace(']', '').replace(';', '').replace(' ', '').replace('\\r', '').replace('\\n', '')
    state = state.split(',')
    f_data = []  # result：最终数据
    Hang = (int)(len(state) / 27)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 27):
            if x == 0:
                f_data.append([])
            f_data[y].append(state[x + y * 27])
    # print(f_data)

    data = f_data
    Get = 0
    Lose = 0
    Hcount = 0
    Gcount = 0
    H_Get = 0
    H_Lose = 0
    G_Get = 0
    G_Lose = 0
    Get_5 = 0
    Lose_5 = 0
    Get_10 = 0
    Lose_10 = 0

    for i in range(Hang):
        Get += int(data[i][3])
        Lose += int(data[i][4])
        if i < 5 :
            Get_5 += int(data[i][3])
            Lose_5 += int(data[i][4])
        if i < 10:
            Get_10 += int(data[i][3])
            Lose_10 += int(data[i][4])
        if (int(data[i][5]) == 1):
            Hcount += 1
            H_Get += int(data[i][3])
            H_Lose += int(data[i][4])
        elif (int(data[i][5]) == 0):
            Gcount += 1
            G_Get += int(data[i][3])
            G_Lose += int(data[i][4])

    f_AveG = round(float(Get / Hang),2)
    f_AveL = round(float(Lose / Hang),2)
    f_AveHG = round(float(H_Get / Hcount),2)
    f_AveHL = round(float(H_Lose / Hcount),2)
    f_AveGG = round(float(G_Get / Gcount),2)
    f_AveGL = round(float(G_Lose / Gcount),2)
    f_AveG5 = round(float(Get_5 / 5), 2)
    f_AveL5 = round(float(Lose_5 / 5), 2)
    f_AveG10 = round(float(Get_10 / 10), 2)
    f_AveL10 = round(float(Lose_10 / 10), 2)

    pattern = re.compile(
        '(?<=var a_data=)[\S\s]+(?=var ma_data)')
    state = re.findall(pattern, str(content))
    state = str(state)
    state = state.replace('\'', '').replace('[', '').replace(']', '').replace(';', '').replace(' ', '').replace('\\r',
                                                                                                                '').replace(
        '\\n', '')
    state = state.split(',')
    a_data = []  # result：最终数据
    Hang = (int)(len(state) / 36)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 36):
            if x == 0:
                a_data.append([])
            a_data[y].append(state[x + y * 36])
    # a_data_df = pd.DataFrame(a_data)
    # pd.set_option('display.max_columns', None)
    # print(a_data_df)
    data = a_data
    Win_5 = 0
    Win_10 = 0
    Handicap_5 = 0
    Handicap_10 = 0
    Big_5 = 0
    Big_10 = 0

    for i in range(Hang):
        if i < 5:
            if ((data[i][9]) == '1'):
                Win_5 += 1
            if ((data[i][12]) == '1'):
                Handicap_5 += 1
            if ((data[i][15]) == '1'):
                Big_5 += 1
        if i < 10:
            if ((data[i][9]) == '1'):
                Win_10 += 1
            if ((data[i][12]) == '1'):
                Handicap_10 += 1
            if ((data[i][15]) == '1'):
                Big_10 += 1

    f_Win_5 = round(float(Win_5 / 5), 2)
    f_Handicap_5 = round(float(Handicap_5 / 5), 2)
    f_Big_5 = round(float(Big_5 / 5), 2)
    f_Win_10 = round(float(Win_10 / 10), 2)
    f_Handicap_10 = round(float(Handicap_10 / 10), 2)
    f_Big_10 = round(float(Big_10 / 10), 2)

    pattern = re.compile(
        '(?<=var h_ranking=)[\S\s]+(?=var g_ranking)')
    state = re.findall(pattern, str(content))
    state = str(state)
    state = state.replace('\'', '').replace('[', '').replace(']', '').replace(';', '').replace(' ', '').replace('\\r', '').replace('\\n', '').replace('\"', '')
    Hrank = state.split(',')
    #print(state)
    pattern = re.compile(
        '(?<=var g_ranking=)[\S\s]+(?=var v_data)')
    state = re.findall(pattern, str(content))
    state = str(state)
    state = state.replace('\'', '').replace('[', '').replace(']', '').replace(';', '').replace(' ', '').replace('\\r', '').replace('\\n', '').replace('\"', '')
    Grank = state.split(',')
    #print(state)

    ranking = [e_AveG, e_AveL, e_AveHG, e_AveHL, e_AveGG, e_AveGL, e_AveG5, e_AveL5, e_AveG10, e_AveL10, e_Win_5,
               e_Handicap_5, e_Big_5, e_Win_10, e_Handicap_10, e_Big_10, ] + Hrank + [f_AveG, f_AveL, f_AveHG, f_AveHL,
                                                                                      f_AveGG, f_AveGL, f_AveG5,
                                                                                      f_AveL5, f_AveG10, f_AveL10,
                                                                                      f_Win_5, f_Handicap_5, f_Big_5,
                                                                                      f_Win_10,
                                                                                      f_Handicap_10, f_Big_10] + Grank
    #print(ranking)

    gameid_list = [gameid]

    result =  gameid_list + playtime + LName + team_name + VS + score + ranking + result1 + result2

    if (float(score[0]) - float(score[1]) > float(result[50])):
        result.insert(8, '1')
    elif (float(score[0]) - float(score[1]) == float(result[50])):
        result.insert(8, '0')
    elif (float(score[0]) - float(score[1]) < float(result[50])):
        result.insert(8, '-1')

    if (float(score[0]) - float(score[1]) > float(result[54])):
        result.insert(9, '1')
    elif (float(score[0]) - float(score[1]) == float(result[54])):
        result.insert(9, '0')
    elif (float(score[0]) - float(score[1]) < float(result[54])):
        result.insert(9, '-1')

    if (float(score[0]) + float(score[1]) > float(result[122])):
        result.insert(10, '1')
    elif (float(score[0]) + float(score[1]) == float(result[122])):
        result.insert(10, '0')
    elif (float(score[0]) + float(score[1]) < float(result[122])):
        result.insert(10, '-1')

    if (float(score[0]) + float(score[1]) > float(result[126])):
        result.insert(11, '1')
    elif (float(score[0]) + float(score[1]) == float(result[126])):
        result.insert(11, '0')
    elif (float(score[0]) + float(score[1]) < float(result[126])):
        result.insert(11, '-1')

    # result = np.array(result)
    # result = result.transpose()
    print(result)

    result_df = pd.DataFrame(result)#, columns=['编号', '时间', '联赛', '主队', '客队', '联赛', '公司1', '初主', '初盘', '初客', '终主', '终盘', '终客', '公司2', '初主', '初盘', '初客', '终主', '终盘', '终客', '公司3', '初主', '初盘', '初客', '终主', '终盘', '终客', '公司4', '初主', '初盘', '初客', '终主', '终盘', '终客', '公司5', '初主', '初盘', '初客', '终主', '终盘', '终客', '公司6', '初主', '初盘', '初客', '终主', '终盘', '终客'])
    result_df = result_df.transpose()

    if (Lname == 'NBA'):
        path = root + '/' + 'NBAdata' + '.xlsx'
    elif(Lname == 'CBA'):
        path = root + '/' + 'CBAdata' + '.xlsx'


    if (os.path.isfile(path)):
        Bdata = pd.read_excel(path)
        result_df = Bdata.append(result_df, ignore_index=True)
    result_df[0] = result_df[0].astype('str')

    result_df = result_df.drop_duplicates(subset=[0], keep='last')
    result_df.sort_values(1, inplace=True)
    result_df.to_excel(path, index=None)

    if (VS[0] == '完'):
        organize.spider_done(gameid,'NBA')
        return