import numpy as np


class PCA:

    # n_components代表要多少个主成分
    def __init__(self, n_components):
        """初始化PCA"""
        assert n_components >= 1, "n_components must be valid"
        self.n_components = n_components
        self.components_ = None

    # k定义梯度上升法中的batch大小
    def fit(self, X, eta=0.01, n_iters=1e4):
        """获得数据集X的前n个主成分"""
        assert self.n_components <= X.shape[1], \
            "n_components must not be greater than the feature number of X"
        assert k >= 1, \
            "the batch size calculated each time must be larger than 1"

        # 均值归0处理
        def demean(X):
            return X - np.mean(X, axis=0)

        # 主成分函数。梯度上升法的目标函数
        def f(w, X):
            return np.sum((X.dot(w) ** 2)) / len(X)

        # 目标函数的导函数
        def df(w, X):
            return X.T.dot(X.dot(w)) * 2. / len(X)

        # 每一次w向量的方向向量化
        def direction(w):
            return w / np.linalg.norm(w)

        #  求出X矩阵的第一主成分，批量梯度上升法
        def first_component(X, initial_w, eta=0.01, n_iters=1e4, epsilon=1e-8):

            w = direction(initial_w)
            cur_iter = 0

            # 样本数m
            m = len(X)

            while cur_iter < n_iters:
                gradient = df(w, X)
                last_w = w
                # 梯度上升
                w = w + eta * gradient
                w = direction(w)
                if (abs(f(w, X) - f(last_w, X)) < epsilon):
                    break

                cur_iter += 1

            return w

        X_pca = demean(X)
        # 主成分矩阵，(k, n)，k是主成分个数，n是特征数
        self.components_ = np.empty(shape=(self.n_components, X.shape[1]))
        for i in range(self.n_components):
            # w不能为0，0向量的运算只能得到0。是目标函数的极小值
            initial_w = np.random.random(X_pca.shape[1])
            w = first_component(X_pca, initial_w, eta, n_iters)
            self.components_[i, :] = w
            # 除去主成分向量的分量
            X_pca = X_pca - X_pca.dot(w).reshape(-1, 1) * w

        return self

    def transform(self, X):
        """将给定的X，映射到各个主成分分量中"""
        # X的特征量要和主成分特征量一致
        assert X.shape[1] == self.components_.shape[1]

        # 转换的方法就是X*WT
        return X.dot(self.components_.T)

    def inverse_transform(self, X):
        """将给定的X，反向映射回原来的特征空间"""
        assert X.shape[1] == self.components_.shape[0]

        return X.dot(self.components_)

    def __repr__(self):
        return "PCA(n_components=%d)" % self.n_components
