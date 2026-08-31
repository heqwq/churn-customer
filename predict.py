import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. 读数据
df = pd.read_excel('客户流失分析.xlsx', sheet_name='Sheet2')

# 2. 选特征（用你实际有的列名）
features = ['Age', 'Total_Purchase', 'Account_Manager', 'Years', 'Num_Sites']
X = df[features]
y = df['Churn']

# 3. 拆分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. 训练模型
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 5. 预测
y_pred = model.predict(X_test)

# 6. 看效果
print("准确率:", accuracy_score(y_test, y_pred))
print("\n分类报告:\n", classification_report(y_test, y_pred))

# 7. 特征重要性
importance = pd.DataFrame({
    '特征': features,
    '系数': model.coef_[0]
})
print("\n特征重要性（系数绝对值越大影响越大）:\n", importance)