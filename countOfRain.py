import csv
count=0
i=1
while i<4:
    s='%s月天气.csv' % i
    with open(s,'r',encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        column1 = [row["天气状况"] for row in reader]
    #找到含有雨字的项并计数
    for x in column1:
        if "雨" in x:
            count+=1
    i+=1
print("下雨天有%s天" % count)
