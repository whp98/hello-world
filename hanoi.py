# 写一个汉诺塔程序
#      函数(次数, 从哪里来, 到哪里去, 辅助)
def hanoi(timesOfMove , nameOffrom, to, helper):
    if timesOfMove == 1:
        print(nameOffrom + '->' + to)
    else:
        hanoi(timesOfMove - 1, nameOffrom, helper, to)
        print(nameOffrom + '->' + to)
        hanoi(timesOfMove - 1, helper, to, nameOffrom)

hanoi(2, 'A', 'B','C')
