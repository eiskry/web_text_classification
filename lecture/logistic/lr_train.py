import ast
import math
import my_function

##### 訓練ステップ
##### 正則化項付きロジスティック回帰の更新

# hyper parameter
rho = 0.5
lam = 0.5
maxit = 2000
tol = 1e-05

# ----- ----- ----- # 
# 重みベクトルwを適当(全て1)に初期化する
def w＿initialize(data):
    w = {}
    for id in data.keys():
        for val in data[id].keys():
                w[val] = 0.5
    return w

# ----- ----- ----- # 
# ロジスティックシグモイド関数
def logi_sig(a):
    value = 1 / (1+(math.exp(-a)))
    return value 

# ----- ----- ----- # 
# 正則化項月ロジスティック回帰の更新し値を使って重みを更新
# 重みに変化がなければ終了
# c = 1 or 0
def update_w(data, w, c):
    tmp = 0
    r = 0
    for i in range(maxit):
        for id in data.keys():
            for val in data[id].keys():
                tmp = logi_sig(data[id][val] * w[val])
                r = rho * (tmp - c) * data[id][val]
                if r < tol:
                    break
                w[val] = (1-lam*rho) * w[val]- r
    return w

