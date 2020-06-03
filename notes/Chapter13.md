# 第 13 章 集成学习和随机森林

## 集成学习

- 多个算法进行计算，然后综合投票，集成决策
- sklearn中有voting classifer

## hard和soft voting classifer

- hard: 少数服从多数
- soft: 更合理的投票应该有权值
  - 将每一个模型分类的概率作为权值

- soft voting就要求集合每一个模型都能估计概率
- 比如逻辑回归算法计算predict_proba
  - 有这个方法就支持soft voting

- kNN也支持概率
- 决策树也支持概率
  - 因为叶子节点不一定是一个类。概率就是叶子节点中占比最高的分类占整个叶子节点样本数的比例

- SVM的SVC看似不支持概率。但是可以通过消耗一定的计算资源计算出概率
  - probability参数设置为true即可算出概率

## 