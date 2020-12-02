import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/tineng/view/form_400Mx5_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('=')[1][:-1]
data = json.loads(data)['form_400Mx5']

url1 = 'https://creator.zoho.com.cn/api/json/tineng/view/form_400Mx5_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('=')[1][:-1]
data1 = json.loads(data1)['form_400Mx5']

data = data+data1

for i in data:
    fie = ['ID', 'form_YunDongYuan', 'form_YunDongYuan_ID', 'form_YunDongYuan_Dropdown_XingBie', 'Date_field_CeShi', 'Single_Line_CeShiDiDian', 'Decimal_1',
           'Decimal_2', 'Decimal_3', 'Decimal_4', 'Decimal_5', 'Formula_PingJunChengJi', 'Number_XinTiao',
           'Dropdown_PingFen', 'Formula_PingFen', 'Multi_Line_BeiZhu']
    val = [str('"'+i['ID']+'"'), str('"'+i['form_YunDongYuan']+'"'), str('"'+i['form_YunDongYuan.ID']+'"'), str('"'+i['form_YunDongYuan.Dropdown_XingBie']+'"'), str('"'+i['Date_field_CeShi']+'"'),
                    str('"'+i['Single_Line_CeShiDiDian']+'"'), str('"'+str(i['Decimal_1'])+'"'), str('"'+str(i['Decimal_2'])+'"'), str('"'+str(i['Decimal_3'])+'"'),
           str('"'+str(i['Decimal_4'])+'"'), str('"'+str(i['Decimal_5'])+'"'), str('"'+str(i['Formula_PingJunChengJi'])+'"'), str('"'+i['Number_XinTiao']+'"'), str('"'+i['Dropdown_PingFen']+'"'),
           str('"'+str(i['Formula_PingFen'])+'"'), str('"'+i['Multi_Line_BeiZhu']+'"')]

    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_400Mx5(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
