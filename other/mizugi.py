# coding: utf-8
n = int(input())
ans = 1
# 9桁まであればよいので，これくらいの桁数以上はいらない
mod = 1000000000000

for i in range(2, n + 1):
    ans *= i
    # 末尾に0 = 10の倍数の時である
    while (ans % 10 == 0):
        ans //= 10
    ans %= mod

# 下から9桁取得，
ans = str(ans)[-9:]
# int型にすれば先頭の0が消える
print(int(ans))
