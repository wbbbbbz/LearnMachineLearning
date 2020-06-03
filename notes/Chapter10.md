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