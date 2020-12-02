import pymysql
import requests
import json
import calendar
import time

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('=')[1][:-1]
data = json.loads(data)['form']

url1 = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('=')[1][:-1]
data1 = json.loads(data1)['form']
data = data + data1
# print(len(data))
for i in data:
    fie = ['ID', 'form_YunDongYuan', 'form_YunDongYuan_ID', 'Single_Line_JiGuan', 'Single_Line_MinZu', 'Dropdown_YunDongDengJi', 'Date_field_KaiShiXunLian',
           'Single_Line_QiMengJiaoLian', 'Single_Line_ShengDuiJiaoLian', 'Single_Line_GuoJiaDuiJiaoLian', 'form_LaiYuanDanWei', 'Rich_Text_RongYu']

    img = ''
    val = [str(i['ID']), str('"'+str(i['form_YunDongYuan'])+'"'), str('"'+str(i['form_YunDongYuan.ID'])+'"'), str('"'+str(i['Single_Line_JiGuan'])+'"'),
           str('"' + str(i['Single_Line_MinZu']) + '"'), str('"'+str(i['Dropdown_YunDongDengJi'])+'"'), str('"'+str(i['Date_field_KaiShiXunLian'])+'"'),
           str('"' + str(i['Single_Line_QiMengJiaoLian']) + '"'),  str('"'+str(i['Single_Line_ShengDuiJiaoLian'])+'"'), str('"'+str(i['Single_Line_GuoJiaDuiJiaoLian'])+'"'),
           str('"' + str(i['form_LaiYuanDanWei']) + '"'), str('"'+str(i['Rich_Text_RongYu'].split('<div>')[1].split('</div>')[0])+'"')]


    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
