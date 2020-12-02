import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_YunDongYuan_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('1571=')[1][:-1]
data = json.loads(data)['form_YunDongYuan']

url1 = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_YunDongYuan_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('1571=')[1][:-1]
data1 = json.loads(data1)['form_YunDongYuan']
data = data + data1
# print(len(data))
for i in data:
    fie = ['ID', 'Single_Line_ZhongWenMing', 'Single_Line_YingWenMing', 'Image_TouXiang', 'Checkbox_YunDongXiangMu', 'Dropdown_ChiPaiShou', 'Dropdown_XingBie',
           'Date_field_ChuSheng','form_DiQu', 'Radio_GuoJiaDuiChengYuan', 'form_ZuZhiJiaGou', 'form_ZuZhiJiaGou_ID', 'Formula_ZuZhiJiaGou', 'Single_Line_MenHuYongHuMing']
    if len(i['Image_TouXiang']) > 0:
        img = i['Image_TouXiang'].split('"')[1]
    else:
        img = ''
    val = [str(i['ID']), str('"'+i['Single_Line_ZhongWenMing']+'"'), str('"'+i['Single_Line_YingWenMing']+'"'), str('"'+img+'"'),
                    str('"'+i['Checkbox_YunDongXiangMu'].split('[')[1].split(']')[0]+'"'), str('"'+i['Dropdown_ChiPaiShou']+'"'), str('"'+i['Dropdown_XingBie']+'"'), str('"'+i['Date_field_ChuSheng']+'"'), str('"'+i['form_DiQu']+'"'),
                    str('"'+i['Radio_GuoJiaDuiChengYuan']+'"'), str('"'+i['form_ZuZhiJiaGou']+'"'), str('"'+i['form_ZuZhiJiaGou.ID']+'"'), str('"'+i['Formula_ZuZhiJiaGou']+'"'), str('"'+i['Single_Line_MenHuYongHuMing']+'"')]


    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_YunDongYuan_Report(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.close()
