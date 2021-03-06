# 封装kNN计算过程
import numpy as np
from math import sqrt
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier


# k代表kNN中的k值
# X_train是numpy中的numpy.array，是X矩阵
# y_train也是numpy.array，是y向量
# x是最终输入的新店，需要预测的点


class KNNClassifier:

    def __init__(self, k):
        """初始化kNN分类器"""
        assert k >= 1, "k must be valid"
        # 保存k值
        self.k = k
        # 保存私有的训练集
        self._X_train = None
        self._y_train = None

    def fit(self, X_train: np.array, y_train: np.array):
        """根据训练数据集X_train和y_train训练kNN分类器"""
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_train"
        assert self.k <= X_train.shape[0], \
            "the size of X_train must be at least k."
        self._X_train = X_train
        self._y_train = y_train
        return self

    def predict(self, X_predict):
        """给定待预测数据集X_predict，返回表示X_predict的结果向量"""
        assert self._X_train is not None and self._y_train is not None, \
            "must fit before predict!"
        # 特征个数必须和训练集中个数一致
        assert X_predict.shape[1] == self._X_train.shape[1], \
            "the feature number of X_predict must be equal to X_train"

        y_predict = [self._predict(x) for x in X_predict]
        return np.array(y_predict)

    # 输入一元的待预测数据，输出单一数字的分类结果
    def _predict(self, x):
        """给定单个待预测数据x，返回x的预测结果值"""
        assert x.shape[0] == self._X_train.shape[1], \
            "the feature number of x must be equal to X_train"
        # 生成x到_X_train各个点的距离
        distances = [sqrt(np.sum((x - _x_train)**2))
                     for _x_train in self._X_train]
        # 索引排序
        nearest = np.argsort(distances)
        # 取出topK
        topK_y = [self._y_train[i] for i in nearest[:self.k]]
        # 进行投票
        votes = Counter(topK_y)
        return votes.most_common(1)[0][0]

    # representor
    def __repr__(self):
        return "KNN(k=%d)" % self.k
