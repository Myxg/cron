import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/xunlian/view/form_ZhouJiHua_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('=')[1][:-1]
data = json.loads(data)['form_ZhouJiHua']

url1 = 'https://creator.zoho.com.cn/api/json/xunlian/view/form_ZhouJiHua_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('=')[1][:-1]
data1 = json.loads(data1)['form_ZhouJiHua']

data = data+data1

# print(len(data))
for i in data:
    fie = ['ID', 'Date_field_KaiShi', 'Date_field_JieShu', 'form_ZuZhiJiaGou', 'form_ZhiYuan_ZhuJiaoLian', 'form_ZhiYuan_JiaoLianZu', 'Single_Line_ZhiDaoSiXiang',
           'Single_Line_YaoQiuJiMuDi', 'Number_KeShi', 'Number_CiShu', 'Dropdown_JiShu', 'Dropdown_LiLiangShenTi', 'Dropdown_ZhuanXiangTiNeng', 'Dropdown_YunDongLiang',
           'Dropdown_QiangDu']

    img = ''
    val = [str(i['ID']), str('"'+str(i['Date_field_KaiShi'])+'"'), str('"'+str(i['Date_field_JieShu'])+'"'), str('"'+str(i['form_ZuZhiJiaGou'])+'"'),
           str('"' + str(i['form_ZhiYuan_ZhuJiaoLian']) + '"'), str('"'+str(i['form_ZhiYuan_JiaoLianZu'].split('[')[1].split(']')[0])+'"'), str('"' + str(i['Single_Line_ZhiDaoSiXiang']) + '"'),
           str('"' + str(i['Single_Line_YaoQiuJiMuDi']) + '"'), str('"' + str(i['Number_KeShi']) + '"'), str('"' + str(i['Number_CiShu']) + '"'),
           str('"' + str(i['Dropdown_JiShu']) + '"'), str('"' + str(i['Dropdown_LiLiangShenTi']) + '"'), str('"' + str(i['Dropdown_ZhuanXiangTiNeng']) + '"'),
           str('"' + str(i['Dropdown_YunDongLiang']) + '"'), str('"' + str(i['Dropdown_QiangDu']) + '"')]


    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_ZhouJiHua(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
