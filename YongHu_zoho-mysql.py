import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_YongHu_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('=')[1][:-1]
data = json.loads(data)['form_YongHu']

url1 = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_YongHu_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('=')[1][:-1]
data1 = json.loads(data1)['form_YongHu']

data = data + data1
# print(len(data))
for i in data:
    fie = ['ID', 'Single_Line_YongHuMing', 'Single_Line_DianHuaHaoMa', 'Query_YunDongYuan', 'Query_YunDongYuan_ID', 'Dropdown_JueSe', 'form_JiaoLian',
           'form_JiaoLian_ID', 'email', 'date_joined']

    img = ''
    val = [str(i['ID']), str('"'+str(i['Single_Line_YongHuMing'])+'"'), str('"'+str(i['Single_Line_DianHuaHaoMa'])+'"'), str('"'+str(i['Query_YunDongYuan'])+'"'),
           str('"' + str(i['Query_YunDongYuan.ID']) + '"'), str('"'+str(i['Dropdown_JueSe'])+'"'), str('"'+str(i['form_JiaoLian'])+'"'),
           str('"' + str(i['form_JiaoLian.ID']) + '"'),  str('"'+str(i['email'])+'"'), str('"'+str(i['date_joined'])+'"')]


    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_YongHu(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
