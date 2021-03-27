https://zhuanlan.zhihu.com/p/68397317

#如果将用户流失率降低5%，公司利润将提升25%-85%
提出问题:
1.分析用户特征与流失的关系。
2.从整体情况看，流失用户的普遍特征。
3.尝试找到合适的模型预测流失用户。
4.针对性给出增加用户黏性、预防流失的建议。

#一 数据清洗
# 完整性——行列完整 合法性 唯一性

#清屏
import os
i=os.system("cls")
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customerDF = pd.read_csv('D:\study\python_study\practice\kaggle\Telco Customer Churn\WA_Fn-UseC_-Telco-Customer-Churn.csv')

customerDF.head(10)

pd.isnull(customerDF).sum(1)

#查看数据类型，将金额的数据类型转换成浮点型数据
customerDF.info()
customerDF['TotalCharges'].astype(float)#ValueError——有缺失
#查看每一列的数据取值
for x in customerDF.columns:
    test=customerDF.loc[:,x].value_counts()
    print(' {0} 的行数是：{1}'.format(x,test.sum()))
    print(' {0} 的内容是：\n{1}\n'.format(x,test))


#强制转换
customerDF['TotalCharges'] = pd.to_numeric(customerDF['TotalCharges'],errors='coerce')

customerDF.dtypes

#查看NaN值对应的部分信息
customerDF.isnull().any()
customerDF[customerDF['TotalCharges'].isnull().values==True][['tenure','MonthlyCharges','TotalCharges']]

#将总消费额填充成月消费额
customerDF.loc[:,'TotalCharges'].replace(to_replace=np.nan,value=customerDF.loc[:,'MonthlyCharges'],inplace=True)
#查看是否替换成功
print(customerDF[customerDF['tenure']==0][['tenure','MonthlyCharges','TotalCharges']])
# 将‘tenure’入网时长从0修改为1
customerDF.loc[:,'tenure'].replace(to_replace=0,value=1,inplace=True)
#再看其类型
print(customerDF['TotalCharges'].dtypes)

# 获取数据类型的描述统计信息
customerDF.describe()


#二、可视化分析：将用户特征分为用户属性，服务属性、合同属性

#先查看流失用户的数量和占比

len(customerDF[customerDF['Churn']=='Yes'])
len(customerDF[customerDF['Churn']=='Yes'])/len(customerDF)

plt.pie(customerDF['Churn'].value_counts(),labels=customerDF['Churn'].value_counts().index)
plt.title('Churn(Yes/No) Ratio')
plt.show()









