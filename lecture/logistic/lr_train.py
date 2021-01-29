import ast
import math
import my_function

##### 訓練ステップ
##### 正則化項付きロジスティック回帰の更新

# hyper parameter
rho = 10
lam = 100
maxit = 2000
tol = 1e-03

# ----- ----- ----- # 
# 重みベクトルwを適当(全て1)に初期化する
def w＿initialize(data):
    w = {}
    for id in data.keys():
        for val in data[id].keys():
                w[val] = 1
    return w


# ----- ----- ----- # 
# 正則化項月ロジスティック回帰の更新し値を使って重みを更新
# 重みに変化がなければ終了
# c = 1 or 0
def update_w(data, w, c):
    for i in range(maxit):
        for id in data.keys():
            tmp = 0
            value1 = 0
            value2 = 0
            value = 0
            r = 0
            for val in data[id].keys():
                value1  = data[id][val] * w[val]
                value = value + value1
            tmp = my_function.logi_sig(value)
            r = rho * (tmp - c)
            for val in data[id].keys():
                value2  = data[id][val] * r
                if value2 < tol:
                    break
                w[val] = (1 - lam * rho) * w[val] - r * data[id][val]
    return w

