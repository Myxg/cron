import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/tineng/view/FMS_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('=')[1][:-1]
data = json.loads(data)['FMS']
url1 = 'https://creator.zoho.com.cn/api/json/tineng/view/FMS_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('=')[1][:-1]
data1 = json.loads(data1)['FMS']
data = data+data1

for i in data:
    fie = ['ID', 'form_YunDongYuan', 'form_YunDongYuan_ID', 'Date_field_CeShiRiQi', 'Dropdown_GuiLei', 'Dropdown_DongZuo', 'Number_PingFen', 'Multi_Line_BeiZhu']
    val = [str('"'+i['ID']+'"'), str('"'+i['form_YunDongYuan']+'"'), str('"'+i['form_YunDongYuan.ID']+'"'), str('"'+i['Date_field_CeShiRiQi']+'"'),
                    str('"'+i['Dropdown_GuiLei']+'"'), str('"'+str(i['Dropdown_DongZuo'])+'"'), str('"'+str(i['Number_PingFen'])+'"'), str('"'+i['Multi_Line_BeiZhu']+'"')]

    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into FMS(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
