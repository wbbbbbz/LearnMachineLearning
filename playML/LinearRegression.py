import numpy as np
from .metrics import r2_score


class LinearRegression:

    def __init__(self):
        """初始化Linear Regression模型"""
        # 系数
        self.coef_ = None
        # 截距
        self.intercept_ = None
        # 包含了系数和截距的向量
        self._theta = None

    # 正规化方程进行fit
    def fit_normal(self, X_train, y_train):
        """根据训练数据集X_train, y_train训练Linear Regression模型"""
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_train"

        # 横向堆叠，在X_train左边堆叠1的列，使得可以用于计算theta
        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        # 求theta
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)

        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def fit_bgd(self, X_train, y_train, eta=0.01, n_iters=1e4):
        """根据训练数据集X_train, y_train, 使用批量梯度下降法训练Linear Regression模型"""
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_train"

        # 计算损失函数J
        def J(theta, X_b, y):
            # 如果损失函数过大，则返回float的最大值，进行异常处理
            try:
                return np.sum((y - X_b.dot(theta)) ** 2) / len(y)
            except:
                return float('inf')

        # 计算损失函数的求导，向量化
        # 这样得出的结果是列向量，(n+1, 1)的向量
        # (n+1, m) dot ((m, n+1) dot (n+1, 1) - (m, 1))
        def dJ(theta, X_b, y):
            return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(y)

        # 梯度下降计算部分
        # eta是学习量，n_iters是最大循环数
        def gradient_descent(X_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):

            theta = initial_theta
            cur_iter = 0

            while cur_iter < n_iters:
                gradient = dJ(theta, X_b, y)
                last_theta = theta
                theta = theta - eta * gradient
                if (abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon):
                    break

                cur_iter += 1

            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = gradient_descent(
            X_b, y_train, initial_theta, eta, n_iters)

        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    # t0, t1用以计算学习率，模拟退火
    # n_iters描述的是对所有样本看几圈。至少整体看几遍
    def fit_sgd(self, X_train, y_train, n_iters=50, t0=5, t1=50):
        """根据训练数据集X_train, y_train, 使用随机梯度下降法训练Linear Regression模型"""
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_train"
        assert n_iters >= 1

        # 对随机的一行直接计算梯度方向，不需要除以m
        def dJ_sgd(theta, X_b_i, y_i):
            return X_b_i * (X_b_i.dot(theta) - y_i) * 2.

        # 随机梯度下降过程
        def sgd(X_b, y, initial_theta, n_iters=5, t0=5, t1=50):

            # 计算学习率，模拟退火
            def learning_rate(t):
                return t0 / (t + t1)

            theta = initial_theta
            # 整体重复次数是n_iters*m
            m = len(X_b)

            # 因为损失函数的值是跳跃的，不一定是递减的
            # 这里不适合使用epsilon进行判断，因为小于epsilon可能只是梯度的问题
            # 所以直接保证循环次数即可
            for i_iter in range(n_iters):
                # 通过乱序排列，保证每一次数据都是乱序的
                indexes = np.random.permutation(m)
                X_b_new = X_b[indexes, :]
                y_new = y[indexes]

                # 使用两重循环，保证每一次循环看所有的样本
                for i in range(m):
                    gradient = dJ_sgd(theta, X_b_new[i], y_new[i])
                    theta = theta - learning_rate(i_iter * m + i) * gradient

            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.random.randn(X_b.shape[1])
        self._theta = sgd(X_b, y_train, initial_theta, n_iters, t0, t1)

        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def predict(self, X_predict):
        """给定待预测数据集X_predict，返回表示X_predict的结果向量"""
        assert self.intercept_ is not None and self.coef_ is not None, \
            "must fit before predict!"
        assert X_predict.shape[1] == len(self.coef_), \
            "the feature number of X_predict must be equal to X_train"

        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return X_b.dot(self._theta)

    def score(self, X_test, y_test):
        """根据测试数据集 X_test 和 y_test 确定当前模型的准确度"""

        y_predict = self.predict(X_test)
        return r2_score(y_test, y_predict)

    def __repr__(self):
        return "LinearRegression()"
