import MeCab as mc
from collections import Counter
import ast

##### 訓練ステップ
##### 教師文書を利用して、各クラス、各単語についてp(w_j, c_i)を求める

# ----- ----- ----- ----- ----- # 関数の定義

def str_dic(x):
    d = x
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "') + '}'
    d2 = ast.literal_eval(d1)
    return d2

# ----- ----- ----- ----- ----- # 教師文書の読み込み

# ----- ----- ----- # train.cleaner_tf.txt
tid = 0
# 教師文書を読み込み
space = {}
for line in open('train.cleaner_tf.txt', 'r'):
    line = line.replace(" \n", "\n")
    line_ = str_dic(line)
    space[tid] = line_
    # print(space[tid])
    tid += 1

# print(space[0]['まし'])

pwej_cleaner = {}
for id in space.keys():
    for val in space[id].keys():
        if (val not in pwej_cleaner):
            pwej_cleaner[val] = space[id][val]
        else:
            pwej_cleaner[val] = pwej_cleaner[val]+space[id][val]

print(pwej_mp3player)

# ----- ----- ----- # train.mp3player_tf.txt
tid = 0
# 教師文書を読み込み
space = {}
for line in open('train.mp3player_tf.txt', 'r'):
    line = line.replace(" \n", "\n")
    line_ = str_dic(line)
    space[tid] = line_
    # print(space[tid])
    tid += 1

# print(space[0]['まし'])

pwej_mp3player = {}
for id in space.keys():
    for val in space[id].keys():
        if (val not in pwej_mp3player):
            pwej_mp3player[val] = space[id][val]
        else:
            pwej_mp3player[val] = pwej_mp3player[val]+space[id][val]
print(pwej_mp3player)