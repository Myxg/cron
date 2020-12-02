import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/xunlian/view/form_XunLianJiHua_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('=')[1][:-1]
data = json.loads(data)['form_XunLianJiHua']

url1 = 'https://creator.zoho.com.cn/api/json/xunlian/view/form_XunLianJiHua_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('=')[1][:-1]
data1 = json.loads(data1)['form_XunLianJiHua']

data = data+data1
# print(len(data))
for i in data:
    fie = ['ID', 'Date_field_XunLianRi', 'Time_KaiShi', 'Time_JieShu', 'form_ZhiYuan_ZhuJiaoLian', 'form_ZhiYuan_JiaoLianZu', 'form_ZuZhiJiaGou',
           'Formula_ZuZhiJiaGou', 'Dropdown_BianGeng', 'form_KeCheng', 'Dropdown_ZhuangTai', 'Single_Line_BianGengYuanYin', 'Number_YingDao', 'Number_ShiDao',
           'Number_ShiJia', 'Number_BingJia', 'Dropdown_ZhiLiang', 'Multi_Line_BeiZhu']

    img = ''
    val = [str(i['ID']), str('"'+str(i['Date_field_XunLianRi'])+'"'), str('"'+str(i['Time_KaiShi'])+'"'), str('"'+str(i['Time_JieShu'])+'"'),
           str('"' + str(i['form_ZhiYuan_ZhuJiaoLian']) + '"'), str('"'+str(i['form_ZhiYuan_JiaoLianZu'].split('[')[1].split(']')[0])+'"'), str('"' + str(i['form_ZuZhiJiaGou']) + '"'),
           str('"' + str(i['Formula_ZuZhiJiaGou']) + '"'), str('"' + str(i['Dropdown_BianGeng']) + '"'), str('"' + str(i['form_KeCheng']) + '"'),
           str('"' + str(i['Dropdown_ZhuangTai']) + '"'), str('"' + str(i['Single_Line_BianGengYuanYin']) + '"'), str('"' + str(i['Number_YingDao']) + '"'),
           str('"' + str(i['Number_ShiDao']) + '"'), str('"' + str(i['Number_ShiJia']) + '"'), str('"' + str(i['Number_BingJia']) + '"'),
           str('"' + str(i['Dropdown_ZhiLiang']) + '"'), str('"' + str(i['Multi_Line_BeiZhu']) + '"')]


    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_XunLianJiHua(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
