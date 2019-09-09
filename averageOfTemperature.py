import csv
import re
count=0
high=0
low=0
i=1
while i<4:
    s='%s月天气.csv' % i
    with open(s,'r',encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        column1 = [row["气温"] for row in reader]
    #print(len(column1))
    for x in column1:
        #找到所有的数字并放入数组
        temp=re.findall(r"\d+\.?\d*",x)
        high+=int(temp[0])
        low+=int(temp[1])
        count+=1
    i+=1
print("平均高温%.2f摄氏度，平均低温%.2f摄氏度" % (high/count,low/count))
