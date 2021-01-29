import ast
import math
import my_function

##### 訓練ステップ
##### 正則化項付きロジスティック回帰の更新

# hyper parameter
rho = 1
lam = 1000
maxit = 2000
tol = 1e-05

# ----- ----- ----- # 
# 重みベクトルwを適当(全て1)に初期化する
def w＿initialize(data):
    w = {}
    for id in data.keys():
        for val in data[id].keys():
            # if (val not in w):
            w[val] = 0.1
    return w


# ----- ----- ----- # 
# 正則化項月ロジスティック回帰の更新し値を使って重みを更新
# 重みに変化がなければ終了
# c = 1 or 0
def update_w(data, w, c):
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
        # for i in range(maxit):
            value2  = data[id][val] * r
            if value2 < tol:
                break
            # w[val] =  w[val] - r * data[id][val]
            w[val] = (1 - lam * rho) * w[val] - r * data[id][val]
    return w

# 各教師データについて重みの変化を計算
def upedata_w_t(data_t, w, c):
    value = 0
    for val in data_t.keys():
        value = value + data_t[value] * w[value]
    logisig = my_function.logi_sig(value)
    for val in data_t.keys():
        change = rho * (logisig - c) * data_t[val]
        if change < tol:
            break
        w[val] = (1 - lam * rho) * w[val] - r * data[val]
    return w

def update_w(data, w, c):
    w_ = {}
    for id in data.keys():
        w_ = upedata_w_t(data[id], w, c)
        update_w(data, w_, c)
    return w_

# 重みの計算
# def calc_r(data, w, c):
#     for id in data.keys():
#         for val in data[id].keys():
#             value1  = data[id][val] * w[val]
#             value = value + value1
#         tmp = my_function.logi_sig(value)
#         r = rho * (tmp - c)
#     return r


    # for id in data.keys():
    #     tmp = 0
    #     value1 = 0
    #     value2 = 0
    #     value = 0
    #     r = 0
    #     for val in data[id].keys():
    #         value1  = data[id][val] * w[val]
    #         value = value + value1
    #     tmp = my_function.logi_sig(value)
    #     r = rho * (tmp - c)
    #     for val in data[id].keys():
    #     # for i in range(maxit):
    #         value2  = data[id][val] * r
    #         if value2 < tol:
    #             break
    #         # w[val] =  w[val] - r * data[id][val]
    #         w[val] = (1 - lam * rho) * w[val] - r * data[id][val]