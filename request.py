import requests
from bs4 import BeautifulSoup
import pandas as pd

a=1
while a<4:
    url = "http://www.tianqihoubao.com/lishi/guangzhou/month/20190%s.html" % a
    response = requests.get(url)

    #print(response)

    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    hd=soup.find("table",{"class":"b"})
    tr_all=hd.find_all("tr")
    data_all=[]
    for i in tr_all:
        td_all=i.find_all("td",limit=3)
        data=[]
        for j in td_all:
            data.append(j.text.replace(" ","").replace("\n",""))
        data_all.append(data)
    data_all=data_all[0:]
    print(len(data_all))

    weather=pd.DataFrame(data_all)
    weather.columns=["日期","天气状况","气温"]
    weather.drop([0],inplace=True)
    s="%s月天气.csv" % a
    weather.to_csv(s,encoding="utf_8_sig")
    print(s,"写入")
    a+=1

