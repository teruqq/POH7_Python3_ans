# coding: utf-8
x, y, z, n = map(int, input().split())
# 切れ目のリスト
tate = [0, x]
yoko = [0, y]
for i in range(n):
    d, a = map(int, input().split())
    # 縦切り,xが変化
    if d == 0:
        tate.append(a)
    # 横切り,yが変化
    else:
        yoko.append(a)

tate.sort()
yoko.sort()
minx = 1001001001
miny = 1001001001
# それぞれ昇順に切れ目が並んでいるので，最短の辺を探す
for i in range(1, len(tate)):
    minx = min(minx, tate[i] - tate[i - 1])
for j in range(1, len(yoko)):
    miny = min(miny, yoko[j] - yoko[j - 1])

print(minx * miny * z)
