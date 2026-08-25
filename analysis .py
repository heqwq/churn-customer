import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 读取数据
df = pd.read_excel('产品销量表.xlsx')
print("数据形状:", df.shape)
print(df.head())

# 2. 查看数据基本情况
print("\n数据类型和缺失值:")
print(df.info())

# 3. 描述性统计
print("\n描述性统计:")
print(df.describe())

# 4. 查看流失客户占比
print("\n流失客户占比:")
print(df['Churn'].value_counts(normalize=True))

# 5. 按年龄段分组看流失率
print("\n不同年龄段客户的流失率:")
age_groups = pd.cut(df['Age'], bins=[20, 30, 40, 50, 60, 70])
churn_by_age = df.groupby(age_groups)['Churn'].mean()
print(churn_by_age)

# 6. 按消费水平分组看流失率
df['Purchase_Level'] = pd.cut(df['Total_Purchase'],
                               bins=[0, 5000, 10000, 15000, 20000],
                               labels=['低', '中', '高', '超高'])
churn_by_purchase = df.groupby('Purchase_Level')['Churn'].mean()
print("\n不同消费水平的客户流失率:")
print(churn_by_purchase)

# 7. 按是否有账户经理分组看流失率
churn_by_manager = df.groupby('Account_Manager')['Churn'].mean()
print("\n有/无账户经理的客户流失率:")
print(churn_by_manager)

# 8. 画图：消费水平与流失率柱状图
plt.figure(figsize=(8, 5))
churn_by_purchase.plot(kind='bar', color=['green', 'yellow', 'orange', 'red'])
plt.title('不同消费水平的客户流失率')
plt.xlabel('消费水平')
plt.ylabel('流失率')
plt.xticks(rotation=0)
plt.show()

# 9. 画图：账户经理与流失率柱状图
plt.figure(figsize=(6, 4))
churn_by_manager.plot(kind='bar', color=['red', 'green'])
plt.title('有/无账户经理的客户流失率')
plt.xlabel('是否有账户经理 (0=无, 1=有)')
plt.ylabel('流失率')
plt.xticks(rotation=0)
plt.show()

# 10. 交叉分析：不同消费水平下，账户经理对流失率的影响
print("\n交叉分析：不同消费水平下，账户经理对流失率的影响")
cross_by_level = df.groupby(['Purchase_Level', 'Account_Manager'])['Churn'].mean().unstack()
print(cross_by_level)