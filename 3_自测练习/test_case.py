#!/usr/bin/env python3

from my_solution import k_means
from my_solution import Point
# 测试用例
def test_solution():
    # 数据集
    x1, x2, x3, x4, x5, x6, x7 = Point(2, 3, 'x1'), \
        Point(1, 2, 'x2'), Point(1, 1, 'x3'), Point(2, 2,'x4'), \
            Point(4, 2,'x5'), Point(4, 1,'x6'), Point(5, 1, 'x7')
    D = [x1, x2, x3, x4, x5, x6, x7]
    
    # 假设K=2，初始时随机选取两个点作为簇的中心
    r1 = r10 = x1
    r2 = r20 = x2
    c1, c2 = set(D), set()
    
    # 正确答案
    correct_solution = '{x6=(4, 1), x7=(5, 1), x5=(4, 2)}', '{x1=(2, 3), x3=(1, 1), x2=(1, 2), x4=(2, 2)}'
    # 程序求解结果
    c1, c2, r1, r2 = k_means(D, r1, r2)
    result=(str(c1), str(c2))
    assert correct_solution == result