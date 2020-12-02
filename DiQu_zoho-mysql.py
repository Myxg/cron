import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_DiQu_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('1572=')[1][:-1]
data = json.loads(data)['form_DiQu']
url1 = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_DiQu_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('1572=')[1][:-1]
data1 = json.loads(data1)['form_DiQu']
data = data + data1
# print(len(data))
for i in data:
    fie = ['ID', 'Single_Line_DiQu', 'Image_QiZhi']

    img = ''
    val = [str(i['ID']), str('"'+str(i['Single_Line_DiQu'])+'"'), str('"'+str(img)+'"')]


    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_DiQu(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
