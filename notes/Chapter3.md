# 第 3 章 Jupyter Notebook, Numpy和Matplotlib

- notebook加载变量只需要一边，之后就会存到内存中
  - 为了可读性，不要在之前的格子提取后面格子的数据
- 不熟悉某个模块或者函数的时候，直接xxxx?，在notebook中就会输出帮助
  - 或者help(xxxx)

## Jupyter Notebook 魔法命令

- %run
  - 运行脚本
  - 并且会加载到内存中，之后还可以调用
  - 调用模块也行(做一个模块__init__.py)

- %timeit
  - 测试性能
  - 只能接一句话
  - 会自动运行多次测试性能
  - 因为测试多次，如果测试中代码运行发生变化的话时间就不正确

- %%timeit
  - 测试整个单元格内的事件
  - %%是区域运行符

- %time
  - 这次不进行多次测试
  <!-- - 输出CPU time和wall time
    - 多线程中wall time(物理世界时间) < CPU time(所有核心加起来的运行时间) -->
  - 运行几个小时的算法测试一次就可以


## Numpy

- python的list中可以存储任意类型的数据
  - 但是效率就会地下
- 可以使用array，存储单一类型
  - 效率提升
  - 但是array只是将存储中的数据当作一个二维数组来看
    - 没有看作向量或者矩阵，也没有匹配向量或者矩阵相关的运算

- 所以就有numpy框架
  - numpy.array，也只能存储一种类型的数据
  - numpy.arange，可以生成浮点数的数列
  - numpy.linspace，也可以生成数列，包括起始点，终止点的指定个数的等差数列
  - numpy.random，随机算法，可以指定np.random.seed()，这样生成的随机数会固定，方便调试
  
- python中list的切片会产生一个新的list
  - 但是*numpy.arrya中的切片是引用，所以修改会对原矩阵进行修改*
  - 如果需要新的副本，使用切片后加上.copy

- 机器学习中的scikit-learn封装的函数接收的都是numpy
  - pandas中有dataframe类型，对数据处理更加方便
  - 可以使用pandas对数据进行预处理之后转化成numpy之后传入
