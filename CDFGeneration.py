import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import statsmodels.api as sm

# 绘制两组数据的CDF图像在一个图片里
# 读取数据文件,并将数据文件转化为数组
filename = 'test.csv'
with open(filename, 'r') as csvFile:
    # 将CSV文件转化为矩阵
    matrix = np.loadtxt(csvFile, delimiter=",", skiprows=0)
    # 将每一列数据存储在数组中
    array1 = matrix[:, 0]
    array2 = matrix[:, 1]
    array3 = matrix[:, 2]
    # 转换数据类型
    Alone = array1.astype(int)
    Mixed = array2.astype(int)
    Avoid = array3.astype(int)

# 使用ECDF函数画CDF曲线
ecdfAlone = sm.distributions.ECDF(Alone)
x1 = np.linspace(min(Alone), max(Alone), 100)
y1 = ecdfAlone(x1)

ecdfMixed = sm.distributions.ECDF(Mixed)
x2 = np.linspace(min(Mixed), max(Mixed), 100)
y2 = ecdfMixed(x2)

ecdfAvoid = sm.distributions.ECDF(Avoid)
x3 = np.linspace(min(Avoid), max(Avoid), 100)
y3 = ecdfAvoid(x3)

line1, = plt.plot(x1, y1, 'g-', label='Alone', linewidth=1)
line2, = plt.plot(x2, y2, 'b--', label='Mixed', linewidth=1)
line3, = plt.plot(x3, y3, 'r-.', label='Avoid', linewidth=1)

plt.legend(bbox_to_anchor=(0.65, 0.3), loc=2, borderaxespad=0., frameon=False)
plt.grid(which='major', axis='y', linestyle='--', linewidth=1)
plt.xlabel('Execution Time')
plt.show()

# 画数据的箱线图
# 设置图案风格
# plt.style.use("ggplot")
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False
# 正常显示中文字符
plt.rcParams['font.sans-serif'] = ['SimHei']
# 新建一个空的DataFrame
df = pd.DataFrame()
# 读取数据
df["Alone"] = Alone
df["Mixed"] = Mixed
df["Avoid"] = Avoid
# 用matplotlib来画出箱型图
plt.boxplot(x=df.values, labels=df.columns, showfliers=False, showmeans=True, meanprops={'marker': 'D', 'markerfacecolor': 'green'},
            medianprops={'linestyle': '--', 'color': 'red'}, boxprops={'color': 'blue'}, whiskerprops={'linestyle': '--'})
plt.grid(which='major', axis='y', linestyle='--', linewidth=1)
plt.ylabel('Execution Time')
plt.show() 