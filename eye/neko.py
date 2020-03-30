# coding: utf-8
s = input()
c = 0
a = 0
t = 0

for ss in s:
    if ss == 'c':
        c += 1
    elif ss == 'a':
        a += 1
    else:
        t += 1

# 元の文字列から何個cat作れるか = catのうち最小のもの
ans = min(c, min(a, t))
# 補うと何個catを作れるか = catのうち最大数に揃える
max_num = max(c, max(a, t))

print(ans)
print(max_num - c)
print(max_num - a)
print(max_num - t)
