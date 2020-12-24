import MeCab as mc
from collections import Counter
import ast
import math
import my_function

##### 訓練ステップ
##### 教師文書を利用して、各クラス、各単語についてp(w_j, c_i)を求める

# smoothing　有効
delta = 1

# ----- ----- ----- # P(wj|ci)を求める
# あるクラスの教師文書の各単語の生起頻度を計算
def train_count_wj(data):
    wj_class = {}
    for id in data.keys():
        for val in data[id].keys():
            if (val not in wj_class):
                wj_class[val] = data[id][val]
            else:
                wj_class[val] = wj_class[val]+data[id][val]
    return wj_class

# あるクラスの教師文書の全単語数を計算
def train_count_word(pwj_class):
    all_words_class = 0
    for id in pwj_class.keys():
        tmp = pwj_class[id] + delta
        all_words_class = all_words_cleaner + tmp
    return all_words_class

# 最終的なP(wj|ci)を計算
def train_pwj_class(pwj_class, all_words_class):
    for id in pwj_class.keys():
        tmp = pwj_class[id] + delta
        pwj_class[id] = tmp / (all_words_class)
