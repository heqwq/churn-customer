项目负责人：常志博

标题：客户流失分析

简介：900+客户数据，运用 Python (Pandas, Matplotlib) 和 FineBI 两种工具进行对比分析，分析流失率与客户年限、账户经理、站点数量的关系，

核心结论：

1.缺乏老客户运营机制，老客户流失率高，8年以上老客户甚至有40%流失率，该现象极其反常需要重视。

2.有经理反而流失率更高，19%流失率，高出5个百分点（分析发现，账户经理更倾向于分配给低消费、短年限的客户，分配策略问题出问题）

（1）	客户出了问题、快流失了才给配个经理，但已经晚了

（2）	经理服务质量不行，配了但没起到留存作用，甚至可能因为对接体验差加速流失

3.站点大于9之后，顾客流失率大幅增加，其中12~15站点处流失全部更多，说明产品复杂度或服务响应速度可能存在问题


以下是通过fine bi数据工具生成的图（由于分析的图不少我就放部分）

<img width="1459" height="868" alt="image" src="https://github.com/user-attachments/assets/9b501f32-8f19-4c41-b0a2-717b4d6ac61c" />

<img width="1828" height="991" alt="image" src="https://github.com/user-attachments/assets/f7f5e367-3f05-47b5-afb7-693be7e9bcb5" />

<img width="1830" height="964" alt="image" src="https://github.com/user-attachments/assets/ea5c1457-b9f4-4801-a78d-379842c03847" />



以下是通过python代码生成的分析图片与预测



<img width="737" height="563" alt="python导出图片（2）" src="https://github.com/user-attachments/assets/f0b8f0ee-6dd1-4b59-87e7-895d6bdc6a44" />
<img width="1031" height="653" alt="python导出图片（1）" src="https://github.com/user-attachments/assets/133ff039-bb57-4615-8dc5-cba316ac7008" />
<img width="1135" height="382" alt="python导出图片" src="https://github.com/user-attachments/assets/e5493951-2014-4711-b1eb-3248960903eb" />
<img width="1085" height="362" alt="image" src="https://github.com/user-attachments/assets/8770d028-7e90-47dd-a0a8-6679a3d24e66" />

<img width="396" height="220" alt="image" src="https://github.com/user-attachments/assets/79db7e36-94f7-4f40-a0b9-b6095cd69074" />

技术栈Python · Pandas · Matplotlib · FineBI · Excel

以下是pdf和仪表板（因为pdf需要下载，我还放了pdf部分图片，PDF 版本包含完整分析报告和仪表板）


<img width="311" height="886" alt="image" src="https://github.com/user-attachments/assets/660c7dac-3dc5-411e-b085-d4ba185498f2" />


[仪表板.pdf](https://github.com/user-attachments/files/31417604/default.pdf)

[消费客户流失报告.pdf](https://github.com/user-attachments/files/31637348/default.pdf)
