# coding: utf-8
n = int(input())
for i in range(n):
    m = int(input()) // 3
    hour = m // 60
    if m % 60 == 0:
        ans_h = (25 - hour) % 24
        ans_m = 0
    else:
        ans_h = (24 - hour) % 24
        ans_m = 60 - (m - (hour * 60))

    print("{0:02}:{1:02}".format(ans_h, ans_m))
