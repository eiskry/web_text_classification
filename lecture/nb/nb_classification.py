import ast
import nb_train
import math

##### 分類ステップ
##### 入力文書xに対して、分類クラスを決定する

# ----- ----- ----- ----- ----- # 関数の定義

def str_dic(x):
    d = x
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "') + '}'
    d2 = ast.literal_eval(d1)
    return d2

# ----- ----- ----- ----- ----- # 1
# 入力文書の各単語に対して、N(w_j, x)を求める

tid = 0
nwjx = {}
for line in open('test_tf.txt', 'r'):
    line = line.replace(" \n", "\n")
    line_ = str_dic(line)
    nwjx[tid] = line_
    tid += 1

# ----- ----- ----- ----- ----- # 2
# 入力文書の各単語に対して、訓練フェースの結果を参照してp(w_j, c_i)を得る

pwj_cleaner = nb_train.pwj_cleaner
pwj_mp3player = nb_train.pwj_mp3player
all_words_cleaner = nb_train.all_words_cleaner
all_words_mp3player = nb_train.all_words_mp3player

for id in nwjx.keys():
    for val in nwjx[id].keys():
        if (val not in pwj_cleaner):
            pwj_cleaner[val] = 1 / all_words_cleaner

for id in nwjx.keys():
    for val in nwjx[id].keys():
        if (val not in pwj_mp3player):
            pwj_mp3player[val] = 1 / all_words_mp3player

# ----- ----- ----- ----- ----- # 3
#　N(w_j, x)とp(w_j, c_i)の情報から分類クラスを決定する

for id in nwjx.keys():
    val_cleaner = 0
    val_mp3player = 0
    for val in nwjx[id].keys():
        tmp = nwjx[id][val]* math.exp(pwj_cleaner[val])
        val_cleaner = val_cleaner + tmp
    for val in nwjx[id].keys():
        tmp = nwjx[id][val]* math.exp(pwj_mp3player[val])
        val_mp3player = val_mp3player + tmp
    output_class = 'cleaner' if val_cleaner > val_mp3player else 'mp3player'
    print( output_class )