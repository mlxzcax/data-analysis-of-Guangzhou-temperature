# data-analysis-of-Guangzhou-temperature
简单的广州市一季度天气数据分析项目

# 任务要求
从广州历史天气预报查询网站爬取广州市2019年第一季度（1、2、3月）的天气状况，包括日 期、天气状况、气温三个属性，然后针对该数据进行简单数据分析：
1. 广州市2019年第一季度有多少天是下雨天？
2. 广州市2019年第一季度平均最低气温是多少，平均最高气温是多少摄氏度？ 
3. 可视化广州市2019年3月的最低温度和最高温度变化曲线。

# 解决思路
首先从指定网页爬取数据并存入csv文件
1. 读出csv文件，在 天气状况 列中遍历，依次判断是否含有“雨”字，如果有即为下雨天。
2. 读出csv文件，在 气温 列中遍历，读出最高温和最低温，分别求和并除以总天数。
3. 绘制图表，图中显示两条线。

## request.py
此脚本的作用是爬虫，并将所需数据写入文件。主要用到了requests来爬取网页，使用beautifulsoup来解析html。最后使用pandas规格化。具体实现步骤见代码注释。
生成文件：
 [一月天气.csv](https://github.com/mlxzcax/data-analysis-of-Guangzhou-temperature/blob/master/1%E6%9C%88%E5%A4%A9%E6%B0%94.csv)
 [二月天气.csv](https://github.com/mlxzcax/data-analysis-of-Guangzhou-temperature/blob/master/2%E6%9C%88%E5%A4%A9%E6%B0%94.csv)
 [三月天气.csv](https://github.com/mlxzcax/data-analysis-of-Guangzhou-temperature/blob/master/3%E6%9C%88%E5%A4%A9%E6%B0%94.csv)
 
## countOfRain.py
此脚本实现雨天计数的功能。将三张表依次遍历，记录“天气状况”中出现“雨”的个数。使用了csv库读取csv文件。
实现效果如图：
![GitHub](https://github.com/mlxzcax/data-analysis-of-Guangzhou-temperature/blob/master/image/image.png"GitHub,Social Coding")
## averageOfTemperature.py
此脚本实现计算最高温和最低温的平均值。只要将“气温”列的两个整数识别并提出，分别求均值。此处用到了re.findall()用来在字符串中找到正则表达式所匹配的所有子串，并返回一个列表。
![GitHub](https://github.com/mlxzcax/data-analysis-of-Guangzhou-temperature/blob/master/image/1568018817.png"GitHub,Social Coding")
## graph.py
在以上的代码基础上，使用matplotlib绘图。
![GitHub](https://github.com/mlxzcax/data-analysis-of-Guangzhou-temperature/blob/master/image/myplot.png"GitHub,Social Coding")
