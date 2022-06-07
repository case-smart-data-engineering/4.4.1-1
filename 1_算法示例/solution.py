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
        # 对每个点，计算距离簇中心点的距离，并将其分配到簇中
        for p in D:
            if distance(p, r1) < distance(p, r2):
                c1.add(p)
            else:
                c2.add(p)

        # 计算新的簇中心
        temp_r1 = Point(
            sum([p.x for p in c1]) / len(c1),
            sum([p.y for p in c1]) / len(c1))
        temp_r2 = Point(
            sum([p.x for p in c2]) / len(c2),
            sum([p.y for p in c2]) / len(c2))
        # 如果簇中心没有变化，则跳出循环
        if temp_r1 == r1 and temp_r2 == r2:
            break
        # 否则，更新簇中心
        else:
            r1, r2 = temp_r1, temp_r2
        _round += 1
    # 返回两个簇及其中心点
    return c1, c2, r1, r2


if __name__ == '__main__':
    # 数据集
    x1, x2, x3, x4, x5, x6, x7 = Point(2, 3, 'x1'), \
        Point(1, 2, 'x2'), Point(1, 1, 'x3'), Point(2, 2,'x4'), \
            Point(4, 2,'x5'), Point(4, 1,'x6'), Point(5, 1, 'x7')
    D = [x1, x2, x3, x4, x5, x6, x7]
    
    # 假设K=2，初始时随机选取两个点作为簇的中心
    r1 = r10 = x1
    r2 = r20 = x2
    c1, c2 = set(D), set()
    # 利用K-Means算法进行簇的聚类
    c1, c2, r1, r2 = k_means(D, r1, r2)
    # 输出两个簇中的点
    print(f'簇1中包含的点: {c1}\n' f'簇2中包含的点: {c2}')
