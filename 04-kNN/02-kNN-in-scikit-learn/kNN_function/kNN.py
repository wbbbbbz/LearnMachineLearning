# 封装kNN计算过程
import numpy as np
from math import sqrt
from collections import Counter

# k代表kNN中的k值
# X_train是numpy中的numpy.array，是X矩阵
# y_train也是numpy.array，是y向量
# x是最终输入的新店，需要预测的点


def kNN_classify(k: int, X_train: np.array, y_train: np.array, x: np.array) -> int:

    # k值的判断
    assert 1 <= k <= X_train.shape[0], "k must be valid"
    # X_train和y_train的次元数判断
    assert X_train.shape[0] == y_train.shape[0], "the size of X_train must equal to the size of y_train"
    # 输入的x的判断
    assert X_train.shape[1] == x.shape[0], "the feature number of x must be equal to X_train"

    # 各点距离计算，欧拉距离
    distances = [sqrt(np.sum((x-x_train)**2)) for x_train in X_train]
    # 使用argsort得到最近距离的索引
    nearest = np.argsort(distances)

    # 使用列表生成式列出最近k个的y
    topK_y = [y_train[i] for i in nearest[:k]]
    # 使用counter进行投票
    votes = Counter(topK_y)

    # 返回最多票数的列别
    return votes.most_common(1)[0][0]
