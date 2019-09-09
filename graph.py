import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import csv
import re
count=0
high=[]
low=[]

#读取文件，得到气温列
s='3月天气.csv'
with open(s,'r',encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    column1 = [row["气温"] for row in reader]
#把高低气温抽出，放到两个数组中
for x in column1:
    temp=re.findall(r"\d+\.?\d*",x)
    high.append(int(temp[0]))
    low.append(int(temp[1]))
    count+=1

#x轴是日期，31个。
x = np.arange(1, 32,1)
#设置所有图中的标记
plt.title("Changes of temperature in 2019.3")
plt.xlabel("Date")
plt.ylabel("Temperature(high);Temperature(low)")
#同时画两条图线
plt.plot(x, high,"x-",label="Temperature(high)")
plt.plot(x, low,"x-",label="Temperature(low)")
#刻画出全部刻度
plt.xticks(x)
plt.grid(True)


plt.show()
