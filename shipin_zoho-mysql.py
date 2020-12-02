import pymysql
import requests
import json
import time
import calendar

t1 = time.localtime(time.time()-86400)
date = ''.join([str(int(t1.tm_mday)), '-', calendar.month_abbr[int(t1.tm_mon)], '-', str(t1.tm_year)])

url = 'https://creator.zoho.com.cn/api/json/saishi/view/form_ShiPin_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Added_Time.After("' + date + '"))'
data = requests.get(url).text
data = data.replace(' ', '').split('1530=')[1][:-1]
data = json.loads(data)['form_ShiPin']

url1 = 'https://creator.zoho.com.cn/api/json/saishi/view/form_ShiPin_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(Modified_Time.After("' + date + '"))'
data1 = requests.get(url1).text
data1 = data1.replace(' ', '').split('1530=')[1][:-1]
data1 = json.loads(data1)['form_ShiPin']

data = data+data1

for i in data:
    fie = ['ID', 'Dropdown_BiSaiJieGuo', 'Date_field_BiSaiRiQi', 'Url', 'Query_SaiShiMingCheng_ID', 'form_YunDongYuan_B1_ID', 'form_YunDongYuan_B2_ID',
           'Single_Line_ShiPinMingCheng','Query_SaiShiMingCheng', 'Formula_InputTimDate', 'Dropdown_BiSaiXiangMu', 'Dropdown_LunCi', 'form_YunDongYuan_ShengLi_2',
           'Dropdown_QueShi', 'form_YunDongYuan_A2','form_YunDongYuan_ShengLi_1', 'form_YunDongYuan_A1', 'form_YunDongYuan_B2', 'form_YunDongYuan_B1',
           'form_YunDongYuan_A1_ID', 'form_YunDongYuan_A2_ID', 'Single_Line_BiFen', 'Added_Time']
    val = [str(i['ID']), str('"'+i['Dropdown_BiSaiJieGuo']+'"'), str('"'+i['Date_field_BiSaiRiQi']+'"'), str('"'+i['Url'].split('"')[1]+'"'), str(i['Query_SaiShiMingCheng.ID']), str('"'+i['form_YunDongYuan_B1.ID']+'"'),
                    str('"'+i['form_YunDongYuan_B2.ID']+'"'), str('"'+i['Single_Line_ShiPinMingCheng']+'"'), str('"'+i['Query_SaiShiMingCheng']+'"'), str('"'+i['Formula_InputTimDate']+'"'), str('"'+i['Dropdown_BiSaiXiangMu']+'"'),
                    str('"'+i['Dropdown_LunCi']+'"'), str('"'+i['form_YunDongYuan_ShengLi_2']+'"'), str('"'+i['Dropdown_QueShi']+'"'), str('"'+i['form_YunDongYuan_A2']+'"'), str('"'+i['form_YunDongYuan_ShengLi_1']+'"'),
                    str('"'+i['form_YunDongYuan_A1']+'"'), str('"'+i['form_YunDongYuan_B2']+'"'), str('"'+i['form_YunDongYuan_B1']+'"'), str('"'+i['form_YunDongYuan_A1.ID']+'"'), str('"'+i['form_YunDongYuan_A2.ID']+'"'),
                    str('"'+i['Single_Line_BiFen']+'"'), str('"'+i['Added_Time']+'"')]

    db = pymysql.connect('video.hbang.com.cn', 'video', 'P@ssw0rd235', 'video')
    cursor = db.cursor()
    sql = "replace into form_ShiPin_Report(" + ','.join(fie) + ") " + "values(" + ','.join(val) + ")"
    cursor.execute(sql)
    db.commit()
    db.rollback()
    db.close()
