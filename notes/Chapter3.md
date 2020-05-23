# 第 3 章 Jupyter Notebook, Numpy和Matplotlib

- notebook加载变量只需要一边，之后就会存到内存中
  - 为了可读性，不要在之前的格子提取后面格子的数据

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
