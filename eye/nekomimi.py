# coding: utf-8

s = input()
s_r = s.replace('cat', '')
# 'cat'を空の文字列に置換して長さがどれだけ減ったかを計算
print((len(s) - len(s_r)) // 3)
