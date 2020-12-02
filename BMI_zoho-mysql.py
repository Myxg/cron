import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/tineng/view/form_BMI_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('=')[1][:-1]
data = json.loads(data)['form_BMI']

url1 = 'https://creator.zoho.com.cn/api/json/tineng/view/form_BMI_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('=')[1][:-1]
data1 = json.loads(data1)['form_BMI']

data = data+data1

for i in data:
    fie = ['ID', 'form_YunDongYuan', 'form_YunDongYuan_ID', 'form_YunDongYuan_Checkbox_YunDongXiangMu', 'Date_field_CeShiRiQi', 'Decimal_ShenGao', 'Decimal_TiZhong',
           'BMI', 'Number_PingFen']
    val = [str('"'+i['ID']+'"'), str('"'+i['form_YunDongYuan']+'"'), str('"'+i['form_YunDongYuan.ID']+'"'), str('"'+i['form_YunDongYuan.Checkbox_YunDongXiangMu'].split('[')[1].split(']')[0]+'"'),
                    str('"'+i['Date_field_CeShiRiQi']+'"'), str('"'+str(i['Decimal_ShenGao'])+'"'), str('"'+str(i['Decimal_TiZhong'])+'"'), str('"'+str(i['BMI'])+'"'),
           str('"'+str(i['Number_PingFen'])+'"')]

    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_BMI(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
