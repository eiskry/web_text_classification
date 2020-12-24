import MeCab as mc
from collections import Counter
import ast
import math

##### 訓練ステップ
##### 教師文書を利用して、各クラス、各単語についてp(w_j, c_i)を求める

# ----- ----- ----- ----- ----- # 関数・deltaの定義
# 特徴抽出結果を受け取り辞書に変換
def str_dic(x):
    d = x
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "') + '}'
    d2 = ast.literal_eval(d1)
    return d2

def read_tf(text):
    tid = 0
    data_name = {}
    for line in text.readline():
        line = line.replace(" \n", "\n")
        line_ = str_dic(line)
        data_name[tid] = line_
        tid += 1


# smoothing　有効
delta = 50
# smoothing を行わない場合
# delta = 0

# ----- ----- ----- # cleanerクラスについてP(wj|ci)を求める
# 学習文書を読み込み
text1 = open("positive_tf.txt", "r", encoding = "utf-8")
# read_tf(text1)

tid = 0
space = {}
for line in open('positive_tf2.txt', 'r'):
    line = line.replace(" \n", "\n")
    line_ = str_dic(line)
    space[tid] = line_
    tid += 1