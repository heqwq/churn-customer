# 8.4 全量客户流失预测结果

# 对全部数据做预测（不是只对测试集）
all_proba = model.predict_proba(X)[:, 1]  # 所有客户的流失概率
all_pred = model.predict(X)               # 所有客户的预测结果（0/1）

# 把预测结果加回原数据
df['预测流失概率'] = all_proba
df['预测是否流失'] = all_pred

# 按流失概率从高到低排序，看Top10
top10 = df.nlargest(10, '预测流失概率')[
    ['Names', 'Age', 'Total_Purchase', 'Account_Manager', 'Years', 'Num_Sites', 
     '预测流失概率', '预测是否流失']
]

print("全量预测结果（按流失概率从高到低）:")
print(top10.to_string(index=False))

# 统计各风险等级人数
df['风险等级'] = pd.cut(df['预测流失概率'], 
                         bins=[0, 0.1, 0.4, 0.7, 1.0],
                         labels=['低危', '中危', '高危', '极高危'],
                         include_lowest=True)

print("\n各风险等级客户数量:")
print(df['风险等级'].value_counts().sort_index())