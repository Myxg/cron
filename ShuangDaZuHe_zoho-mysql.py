import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])


url = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_ShuangDaZuHe_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('=')[1][:-1]
data = json.loads(data)['form_ShuangDaZuHe']

url1 = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_ShuangDaZuHe_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('=')[1][:-1]
data1 = json.loads(data1)['form_ShuangDaZuHe']

data = data+data1
# print(len(data))
for i in data:
    fie = ['ID', 'Single_Line_MingCheng', 'Single_Line1', 'Dropdown_XiangMu', 'form_YunDongYuan_A', 'form_YunDongYuan_A_ID', 'form_YunDongYuan_B',
           'form_YunDongYuan_B_ID', 'form_DiQu', 'form_ZuZhiJiaGou', 'form_ZuZhiJiaGou_ID', 'Formula_ZuZhiJiaGou']

    img = ''
    val = [str(i['ID']), str('"'+str(i['Single_Line_MingCheng'])+'"'), str('"'+str(i['Single_Line1'])+'"'), str('"'+str(i['Dropdown_XiangMu'])+'"'),
           str('"' + str(i['form_YunDongYuan_A']) + '"'), str('"'+str(i['form_YunDongYuan_A.ID'])+'"'), str('"'+str(i['form_YunDongYuan_B'])+'"'),
           str('"' + str(i['form_YunDongYuan_B.ID']) + '"'),  str('"'+str(i['form_DiQu'])+'"'), str('"'+str(i['form_ZuZhiJiaGou'])+'"'),
           str('"' + str(i['form_ZuZhiJiaGou.ID']) + '"'), str('"'+str(i['Formula_ZuZhiJiaGou'])+'"')]


    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_ShuangDaZuHe(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
