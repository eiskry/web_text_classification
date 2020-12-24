import MeCab as mc
from collections import Counter
import ast
import math
import my_function

##### 訓練ステップ
##### 教師文書を利用して、各クラス、各単語についてp(w_j, c_i)を求める

# ----- ----- ----- ----- ----- # 関数・deltaの定義
# 特徴抽出結果を受け取り辞書に変換
def str_dic(x):
    d = x
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "').replace('"":"', '":"') + '}'
    d2 = ast.literal_eval(d1)
    return d2

def read_tf(text):
    tid = 0
    space = {}
    for line in text:
        line = line.replace(" \n", "\n")
        line_ = str_dic(line)
        space[tid] = line_
        tid += 1
    return space


# smoothing　有効
delta = 50
# smoothing を行わない場合
# delta = 0

# ----- ----- ----- # cleanerクラスについてP(wj|ci)を求める
# 学習文書を読み込み
text1 = open("positive_tf.txt", "r")
positive_tf_data = read_tf(text1)
# print(positive_tf_data[0])

text1 = open("negative_tf.txt", "r")
positive_tf_data = read_tf(text1)
# print(positive_tf_data[0])

# tid = 0
# space = {}
# for line in open('positive_tf.txt', 'r'):
#     line = line.replace(" \n", "\n")
#     line_ = str_dic(line)
#     space[tid] = line_
#     tid += 1
# print(space[0])


# ----- ----- ----- ----- ----- # 1
# データセットを n 個のブロックに分割する.
n=5

# positive_tf
text = open("positive_tf.txt", "r")
pos_data = my_function.read_tf(text)
pos_size = len(pos_data)


s=3
e=4

# partial_pos={}
# for j in range(e):
#     partial_pos[j] = ''
# print(partial_pos)

# for j in range(s, e+1):
#     print(j-s+1)

tmp = my_function.make_partial_data(pos_data,s, e)
print(tmp)
partial_pos={}
s = 0
for i in range(n):
    i = i+1
    e = int(pos_size/n * i)
    partial_pos[i-1] = my_function.partial_data(pos_data, s, e)
    print(s, e)
    s = e + 1

# print(partial_pos[0])
# for j in range(s, e):
#     print(pos_data[j])

# print(pos_data[e])

# for i in range(n):
#     e = int(pos_size/n *i)
#     print(e)
#     for j in range(s, e):
#         partial_pos[i][j-j+1] = pos_data[j]
#     s = e + 1
