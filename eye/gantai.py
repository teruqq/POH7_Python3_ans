# coding: utf-8

n = int(input())
m1 = int(input())
have = [int(i) for i in input().split()]

m2 = int(input())
sell = [int(i) for i in input().split()]
buy = []

# 売り物で持っていないものをチェック
for i in sell:
    if i not in have:
        buy.append(i)

# 買うものがある時は出力
if buy:
    # 昇順に出力する必要(入出力例には無いがテストケースでは有る,せこい)
    buy.sort()
    for i in range(len(buy)):
        if i != (len(buy) - 1):
            print(buy[i], end=" ")
        else:
            print(buy[i])
else:
    print('None')
