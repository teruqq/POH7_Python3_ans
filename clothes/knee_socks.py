# coding: utf-8
n = int(input())
m = int(input())
# Trueの時はR, Falseの時はWを出力
red = True
for i in range(1, m + 1):
    if red:
        print('R', end="")
    else:
        print('W', end="")
    # n回ごとに出力変更
    if i % n == 0:
        red = not red

print()
