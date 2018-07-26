import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import statsmodels.api as sm

# 绘制两组数据的CDF图像在一个图片里
# 读取数据文件,并将数据文件转化为数组
filename = 'onlineOnlyTest180719.csv'
with open(filename, 'r') as csvFile:
    # 将CSV文件转化为矩阵
    matrix = np.loadtxt(csvFile, delimiter=",", skiprows=0)
    # 将每一列数据存储在数组中
    array1 = matrix[:, 0]
    array2 = matrix[:, 1]
    array3 = matrix[:, 2]
    array4 = matrix[:, 3]
    array5 = matrix[:, 4]
    # 转换数据类型
    Test1 = array1.astype(int)
    Test2 = array2.astype(int)
    Test3 = array3.astype(int)
    Test4 = array4.astype(int)
    Test5 = array5.astype(int)

# 使用ECDF函数画CDF曲线
ecdfAlone = sm.distributions.ECDF(Test1)
x1 = np.linspace(min(Test1), max(Test1), 100)
y1 = ecdfAlone(x1)

ecdfMixed = sm.distributions.ECDF(Test2)
x2 = np.linspace(min(Test2), max(Test2), 100)
y2 = ecdfMixed(x2)

ecdfAvoid = sm.distributions.ECDF(Test3)
x3 = np.linspace(min(Test3), max(Test3), 100)
y3 = ecdfAvoid(x3)

ecdfAvoid = sm.distributions.ECDF(Test4)
x4 = np.linspace(min(Test4), max(Test4), 100)
y4 = ecdfAvoid(x4)

ecdfAvoid = sm.distributions.ECDF(Test5)
x5 = np.linspace(min(Test5), max(Test5), 100)
y5 = ecdfAvoid(x5)

line1, = plt.plot(x1, y1, 'g-', label='Test1', linewidth=1)
line2, = plt.plot(x2, y2, 'b--', label='Test2', linewidth=1)
line3, = plt.plot(x3, y3, 'r-.', label='Test3', linewidth=1)
line4, = plt.plot(x4, y4, 'y--', label='Test4', linewidth=1)
line5, = plt.plot(x5, y5, 'c-.', label='Test5', linewidth=1)

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
df["Test1"] = Test1
df["Test2"] = Test2
df["Test3"] = Test3
df["Test4"] = Test4
df["Test5"] = Test5
# 用matplotlib来画出箱型图
plt.boxplot(x=df.values, labels=df.columns, showfliers=True, whis=6, showmeans=True, meanprops={'marker': 'D', 'markerfacecolor': 'green'},
            medianprops={'linestyle': '--', 'color': 'red'}, boxprops={'color': 'blue'}, whiskerprops={'linestyle': '--'})
plt.grid(which='major', axis='y', linestyle='--', linewidth=1)
plt.ylabel('Execution Time')
plt.show()