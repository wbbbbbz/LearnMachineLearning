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

## 集成学习的局限

- 虽然有很多机器学习方法，但是从投票的角度看，仍然不够多
  - 所以要创建子模型，集成更多子模型的意见
  - 子模型之间不能一致，子模型之间要有差异性

- 如何创建差异性？
  - 每个子模型只看样本数据的一部分
  - 每个子模型不需要太高的准确率(因为训练数据集下降了)
    - 当然还是需要比平均水平高
  - 随着子模型数量增多，集成学习的整体准确率会增高
    - 所以集成学习威力巨大，很多场景都会使用

- 集成非参数学习模型，更能产生差异比较大的子模型，有很多参数的不同
  - 成百上千的子模型的时候，首选就是决策树(参数，剪枝等等很多参数不同)

### Bagging 和 Pasting

- 每个子模型只看样本数据的一部分
  - 取样：放回取样Bagging，不放回取样Pasting
  - 一般使用Bagging
  - Bagging不受随机影响
  - 统计学中放回取样：bootstrap
- sklearn中集成为Bagging

## OOB Out-of-Bag

- 放回取样导致一部分样本很有可能没有取到
  - 平均大约有37%的样本没有取到：Out-of-Bag
  - 每一个样本抽不到的概率时1/e
    - [BootstrapSample(有放回抽样)_cholocatehe的专栏-CSDN博客_怎么实现bootstrap有放回](https://blog.csdn.net/cholocatehe/article/details/42130341)

- 所以干脆不适用测试数据集，而使用这部分没有取到的样本左测试/验证
  - sklearn中有oob.score_参数

## Bagging的更多探讨

- Bagging的思路极易并行化处理
  - sklearn中有n_jobs的参数

- 针对特征进行随机采样Random Subspaces
  - 样本特征非常多的情况，比如图像识别，像素点特征特别多
  - 每一次取样是在子空间中取样

- 既针对样本，又针对特征进行随机采样Random Patches
  - 既在行方向上取样，又在列方向上取样
  - sklearn中有bootstarap_features(特征)，max_features

- 不想取样的时候只要将max_samples或max_features填入实际samples数和features数即可

## 随机森林

- 由多个决策树组成的随机森林
  - Base Estimator: Decision Tree

- sklearn封装了随机森林类RandomForestClassifier
  - sklearn的默认随机森林的决策树在节点划分上，在随机的特征子集上寻找最优划分特征。
    - 这种随机性使得子模型的随机性增大

- 极其随机森林Extra-Trees
  - 决策树在节点划分上，使用随机的特征和随机的阈值
  - sklearn中ExtraTreesClassifier
  - 提供额外的随机性，抑制过拟合，但增大了bias
  - 增加偏差，抑制方差
  - 更快的训练速度

## 集成学习解决回归问题
- sklearn中baggingregressor, randomforestregressor, extratreesregressor

## Boosting

- 另一种集成模型的方法
  - 每个模型都在尝试增强(Boosting)整体的效果
- 也可以解决回归问题

### Ada Boosting

- 每一次生成的子模型都是为了弥补上一个子模型学习中的错误
  - 错误分类的点权重增加
  - sklearn中的adaboostclassifier

### Gradient Boosting

- 训练一个模型m1，产生错误e1
  - 针对e1训练第二个模型m2，产生错误e2
  - 针对e2训练第二个模型m3，产生错误e3
  - 最终预测结果是m1+m2+m3...

- sklearn中的gradientboostingclassifier

