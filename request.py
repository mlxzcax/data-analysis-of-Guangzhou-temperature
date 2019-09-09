import requests
from bs4 import BeautifulSoup
import pandas as pd

a=1
#相同方法读取三个网页
while a<4:
    url = "http://www.tianqihoubao.com/lishi/guangzhou/month/20190%s.html" % a
    #获取网页源代码
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    #获得表格中的前三列
    hd=soup.find("table",{"class":"b"})
    tr_all=hd.find_all("tr")
    data_all=[]
    for i in tr_all:
        td_all=i.find_all("td",limit=3)
        data=[]
        for j in td_all:
            #去除源数据中的空格和回车
            data.append(j.text.replace(" ","").replace("\n",""))
        data_all.append(data)
    #去除表格表头
    data_all=data_all[0:]
    #生成规格化的csv文件
    weather=pd.DataFrame(data_all)
    weather.columns=["日期","天气状况","气温"]
    weather.drop([0],inplace=True)
    s="%s月天气.csv" % a
    weather.to_csv(s,encoding="utf_8_sig")
    print(s,"写入")
    a+=1

