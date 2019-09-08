import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import csv
import re
count=0
high=[]
low=[]


s='3月天气.csv'
with open(s,'r',encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    column1 = [row["气温"] for row in reader]
#print(len(column1))
for x in column1:
    temp=re.findall(r"\d+\.?\d*",x)
    high.append(int(temp[0]))
    low.append(int(temp[1]))
    count+=1


x = np.arange(1, 32,1)

#y = high
#z=low
plt.title("Changes of temperature in 2019.3")
plt.xlabel("Date")
plt.ylabel("Temperature(high);Temperature(low)")
plt.plot(x, high,"x-",label="Temperature(high)")
plt.plot(x, low,"x-",label="Temperature(low)")

plt.xticks(x)
plt.grid(True)
#plt.legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)

plt.show()