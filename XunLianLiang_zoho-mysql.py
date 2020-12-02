import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/xunlian/view/form_XunLianLiang_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('=')[1][:-1]
data = json.loads(data)['form_XunLianLiang']

url1 = 'https://creator.zoho.com.cn/api/json/xunlian/view/form_XunLianLiang_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('=')[1][:-1]
data1 = json.loads(data1)['form_XunLianLiang']

data = data + data1
# print(len(data))
for i in data:
    fie = ['ID', 'form_YunDongYuan', 'Formula_ZuZhiJiaGou', 'Date_field_XunLianRiQi', 'Dropdown_XunLianKeMu', 'Number_XunLianShiChang']

    img = ''
    val = [str(i['ID']), str('"'+str(i['form_YunDongYuan'])+'"'), str('"'+str(i['Formula_ZuZhiJiaGou'])+'"'), str('"'+str(i['Date_field_XunLianRiQi'])+'"'),
           str('"' + str(i['Dropdown_XunLianKeMu']) + '"'), str('"'+str(i['Number_XunLianShiChang'])+'"')]


    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_XunLianLiang(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
