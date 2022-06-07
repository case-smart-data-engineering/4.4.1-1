import math


# 定义点类
class Point:
    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        self.name = name

    # 字符串表示
    def __repr__(self):
        return f'{self.name}=({self.x}, {self.y})'

    # 实现 == 操作符
    def __eq__(self, o):
        return isinstance(o, Point) and self.x == o.x and self.y == o.y
    
    # 实现hash
    def __hash__(self):
        return hash((self.x, self.y))

# 计算两个点的距离
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def k_means(D, r1, r2):
    # K=2,初始化2个簇
    c1, c2 = set(), set()
    
    # 迭代计算簇，直到簇中心不再变化
    _round = 1  # 迭代轮数
    while True:
        # 清空簇
        c1.clear()
        c2.clear()
        # 对每个点，计算距离簇中心点的距离，并将其分配到簇中，并计算新的簇中心点
        raise NotImplementedError("对每个点，计算距离簇中心点的距离，并将其分配到簇中，并计算新的簇中心点")
    # 返回两个簇及其中心点
    return c1, c2, r1, r2


if __name__ == '__main__':
    pass
