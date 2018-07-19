# 写一个汉诺塔程序
#      函数(次数, 从哪里来, 到哪里去, 辅助)
def henio(timesOfMove , nameOffrom, to, helper):
    if timesOfMove == 1:
        print(nameOffrom + '->' + to)
    else:
        henio(timesOfMove - 1, nameOffrom, helper, to)
        print(nameOffrom + '->' + to)
        henio(timesOfMove - 1, helper, to, nameOffrom)

henio(1, 'A', 'B','C')