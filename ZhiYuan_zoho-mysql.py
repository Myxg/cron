import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_ZhiYuan_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('=')[1][:-1]
data = json.loads(data)['form_ZhiYuan']

url1 = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_ZhiYuan_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('=')[1][:-1]
data1 = json.loads(data1)['form_ZhiYuan']

data = data + data1
# print(len(data))
for i in data:
    fie = ['ID', 'Image_TouXiang', 'Single_Line_XingMing', 'Dropdown_ZhiWu', 'Single_Line_JianJie', 'form_ZuZhiJiaGou', 'form_ZuZhiJiaGou_ID']

    img = ''
    val = [str(i['ID']), str('"'+str(i['Image_TouXiang'])+'"'), str('"'+str(i['Single_Line_XingMing'])+'"'),
           str('"'+str(i['Dropdown_ZhiWu'])+'"'), str('"'+str(i['Single_Line_JianJie'])+'"'),
           str('"'+str(i['form_ZuZhiJiaGou'].split('[')[1].split(']')[0])+'"'), str('"'+str(i['form_ZuZhiJiaGou.ID'].split('[')[1].split(']')[0])+'"')]


    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_ZhiYuan(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
