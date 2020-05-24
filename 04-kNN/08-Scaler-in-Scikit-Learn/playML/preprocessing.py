import numpy as np


class StandardScaler:

    def __init__(self):
        self.mean_ = None
        self.scale_ = None

    def fit(self, X):
        """根据训练数据集X获得数据的均值和方差"""
        # 暂时只处理二维数据
        assert X.ndim == 2, "The dimension of X must be 2"

        # 对每一列求均值和标准差
        self.mean_ = np.array([np.mean(X[:, i]) for i in range(X.shape[1])])
        self.scale_ = np.array([np.std(X[:, i]) for i in range(X.shape[1])])

        return self

    def transform(self, X):
        """将X根据这个StandardScaler进行均值方差归一化处理"""
        assert X.ndim == 2, "The dimension of X must be 2"
        # transform之前必须进行fit
        assert self.mean_ is not None and self.scale_ is not None, \
            "must fit before transform!"
        # 保证列数相等
        assert X.shape[1] == len(self.mean_), \
            "the feature number of X must be equal to mean_ and std_"

        resX = np.empty(shape=X.shape, dtype=float)
        # 对每一列进行标准化处理
        for col in range(X.shape[1]):
            resX[:, col] = (X[:, col] - self.mean_[col]) / self.scale_[col]
        return resX


class MinMaxScaler:

    def __init__(self):
        self.max_ = None
        self.min_ = None

    def fit(self, X):
        """根据训练数据集X获得数据的最大值和最小值"""
        # 暂时只处理二维数据
        assert X.ndim == 2, "The dimension of X must be 2"

        # 对每一列求均值和标准差
        self.max_ = np.array([np.max(X[:, i]) for i in range(X.shape[1])])
        self.min_ = np.array([np.min(X[:, i]) for i in range(X.shape[1])])

        return self

    def transform(self, X):
        """将X根据这个MinMaxScaler进行最大值最小值归一化处理"""
        assert X.ndim == 2, "The dimension of X must be 2"
        # transform之前必须进行fit
        assert self.max_ is not None and self.min_ is not None, \
            "must fit before transform!"
        # 保证列数相等
        assert X.shape[1] == len(self.max_), \
            "the feature number of X must be equal to mean_ and std_"

        resX = np.empty(shape=X.shape, dtype=float)
        # 对每一列进行标准化处理
        for col in range(X.shape[1]):
            resX[:, col] = (X[:, col] - self.min_[col]) / \
                (self.max_[col] - self.min_[col])
        return resX
