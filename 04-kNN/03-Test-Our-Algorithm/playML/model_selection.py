import numpy as np

# 数据集X，y，测试数据的比例，默认0.2


def train_test_split(X, y, test_ratio=0.2, seed=None):
    """将数据 X 和 y 按照test_ratio分割成X_train, X_test, y_train, y_test"""
    assert X.shape[0] == y.shape[0], \
        "the size of X must be equal to the size of y"
    assert 0.0 <= test_ratio <= 1.0, \
        "test_ration must be valid"

    # 希望结果前后一致的时候，用户传入seed，就是用这个随机种子
    if seed:
        np.random.seed(seed)

    # 生成乱序的索引值
    shuffled_indexes = np.random.permutation(len(X))

    # 测试数据集的大小
    test_size = int(len(X) * test_ratio)
    test_indexes = shuffled_indexes[:test_size]
    train_indexes = shuffled_indexes[test_size:]

    X_train = X[train_indexes]
    y_train = y[train_indexes]

    X_test = X[test_indexes]
    y_test = y[test_indexes]

    return X_train, X_test, y_train, y_test
