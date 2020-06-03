# 第 10 章 分类算法的评价

## 分类准确度的问题

- 对于极度偏斜(Skewed Data)的数据，只是用分类准确度是远远不够的
  - 比如发病率是0.1%的疾病，直接预测所有人都健康的模型都能达到99.9%
  - 也就是如果算法如果达到了99%分类准确度都没有意义

## 混淆矩阵(Confusion Matrix)

- 行代表真实值，列代表预测值
  - 0 - Negative, 1 - Positive
  - 行是第一个维度，真实值放在前面
  - (0, 0)：预测negative正确，TN(True Negative)
  - (0, 1)：预测positive错误，FP(False Positive)
  - (1, 0)：预测negative错误，FN(False Negative)
  - (1, 1)：预测positive正确，TP(True Positive)

## 精准率和召回率

- 精准率Precision
  - TP/(TP+FP)
  - 预测为P的时候TP的概率
  - 因为一般模型中positive是想关注的问题。
  - 预测正确的概率
  - 如果分母为0(不进行预测)则定义为0，因为没有意义

- 召回率recall
  - TP/(TP+FN)
  - 分母是真实值为1的总数量，TP是正确预测positive的数量
  - 真实发生的事件中正确预测的概率是多少
  - positive事件正确预测的概率

- 精准率和召回率在极度偏斜的数据时比分类准确度更有用的

### 解读精准率和召回率

- 根据数据和目的对精准率和召回率进行解读
  - 比如股票预测中注重精准率
  - 比如病人诊断中召回率比较重要

- 如果想兼顾精准率和召回率，就是用F1 Score
  - F1 =  (2*precision*recall)/(precision+recall)
  - 分母为0时定义为0
  - F1是精准率和召唤率的调和平均数
  - 算术平均值的话是两个值的影响
  - 调和平均值的话如果一个值特别小，那么会受该值影响F1也特别小
    - 只有当两个值都比较大的时候，F1才比较大

## Precision-Recall的平衡

- 决策边界可以写成θT.dot(xb)=threshold
- 这样的话可以平移决策边界，只有大于threshold的时候才会被分类进某个分类
- 此时引入一个新的超参数threshold
- 改变threshold时可以改变精准率和召回率
  - threshold偏向于positive一边的时候，精准率变高，召回率变低
  - threshold偏向于negative一边的时候，精准率变低，召回率变高
  - threshold增高：必须由高概率的时候才判断为positive
  - threshold变低：只要有一点概率都判断为positive

