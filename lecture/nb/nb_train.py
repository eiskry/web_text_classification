import MeCab as mc
from collections import Counter
import ast

##### 訓練ステップ
##### 教師文書を利用して、各クラス、各単語についてp(w_j, c_i)を求める

# ----- ----- ----- ----- ----- # 関数の定義
class Vec():
    # def __init__(self, c , magnitude):
    def __init__(self, x, c ):
        self.x = x
        self.c = c
        # self.magnitude = magnitude

# ベクトル用のクラス（Vec）を定義し，各ベクトルに対して，分類クラス（cleaner かmp3player）の
# 情報や，ベクトルの大きさをもつインスタンスを生成できるようにしている．


# ----- ----- ----- ----- -----
def str_dic(x):
    d = x
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "') + '}'
    d2 = ast.literal_eval(d1)
    return d2

# 文書のベクトルを読み込み、クラスラベルを付与する
def read_vec(x, label):
    # x_ = str_dic(x)
    x_vector = Vec(x, label)
    return x_vector

# 入力文書のベクトルを読み込む
def read_input_vec(x):
    x_ = str_dic(x)
    return x_

# 類似度を計算する
def sim(x1, x2):
    sum = 0
    for kye in x1.keys():
        if (kye in x2):
            sum += x1[kye]*x2[kye]
    v1_ = 0
    for value in x1.values():
        v1_ += value*value
    v1 = math.sqrt(v1_)
    v2_ = 0
    for value in x2.values():
        v2_ += value*value
    v2 = math.sqrt(v2_)
    return sum/(v1*v2)

    

# ----- ----- ----- ----- ----- # 教師文書の読み込み
# tid = 0
# # 教師文書を読み込み
# space = {}
# for line in open('train.cleaner_tf.txt', 'r'):
#     line = line.replace(" \n", "\n")
#     line_ = str_dic(line)
#     space[tid] = line_
#     # print(space[tid])
#     tid += 1

tid = 0
# 教師文書を読み込み
space = {}
all_data = ''
for line in open('train.cleaner.txt', 'r'):
    line = line.replace("\n", "")
    all_data = all_data+line

print(all_data)
# ----- ----- ----- ----- ----- # 教師文書の読み込み


# tid = 0
# # 教師文書2を読み込み
# for line in open('train.mp3player.vec=tfidf.txt', 'r'):
#     line_ = str_dic(line)
#     space[tid] = read_vec( line_, 'mp3player')
#     tid += 1
