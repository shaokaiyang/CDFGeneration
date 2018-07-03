import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

filename = 'data-offline.csv' #CSV文件路径

lines = []
with open(filename,'r') as f:
    lines = f.read().split('\n')

dataSets = []

for line in lines:
    # print(line)
    try:
        dataSets.append(line.split(','))
    except :
        print("Error: Exception Happened... \nPlease Check Your Data Format... ")

temp = []
for set in dataSets:
    temp2 = []
    for item in set:
        if item!='':
            temp2.append(float(item))
    temp2.sort()
    temp.append(temp2)
dataSets = temp

for set in dataSets:

    plotDataset = [[],[]]
    count = len(set)
    for i in range(count):

        plotDataset[0].append(float(set[i]))
        plotDataset[1].append((i+1)/count)
    print(plotDataset)
    plt.plot(plotDataset[0], plotDataset[1], '-', linewidth=2)

plt.show()


# 设置图案风格
plt.style.use("ggplot")
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False
# 正常显示中文字符
plt.rcParams['font.sans-serif']=['SimHei']

# 新建一个空的DataFrame
df = pd.DataFrame()

# 读取数据
df["offline"] = [49,143,63,178,184,184,90,132,145,126,132,122,95,102,132,121,114,169,174,177,174,175,168,280,278,270,275,145,176,170,182,190,175,156,16,19,23,23,22,23,25,26,23,24,56,34,41,25,34,35,41]
df["offlineMix"] = [56,153,95,168,194,164,135,142,155,156,142,152,155,142,122,131,144,179,179,179,194,185,188,286,278,277,285,155,186,179,189,199,179,159,26,29,29,33,32,43,28,27,26,29,66,44,47,26,39,39,48]
#df["kmeans"] = [16,19,23,23,22,23,25,26,23,24,56,34,41,25,34,35,41]

# 用matplotlib来画出箱型图
plt.boxplot(x=df.values, labels=df.columns, showfliers=False)
plt.show()

# 用pandas自带的画图工具更快
#df.boxplot()
#plt.show()