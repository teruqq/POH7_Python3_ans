# coding: utf-8

# 左上座標が引数, m*mの範囲が一致しているかをチェック
def check_pattern(x, y):
    for i in range(m):
        for j in range(m):
            nx = x + i
            ny = y + j
            if image[nx][ny] != check[i][j]:
                return False
    return True


n = int(input())
image = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
check = [[int(i) for i in input().split()] for _ in range(m)]

for i in range(n - m + 1):
    for j in range(n - m + 1):
        if check_pattern(i, j):
            print(i, j)
