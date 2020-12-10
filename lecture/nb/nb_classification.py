import ast
import nb_train

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
# 教師文書を読み込み
nwjx = {}
for line in open('test_tf.txt', 'r'):
    line = line.replace(" \n", "\n")
    line_ = str_dic(line)
    nwjx[tid] = line_
    # print(space[tid])
    tid += 1
# print(nwjx[0])

# ----- ----- ----- ----- ----- # 2
# 入力文書の各単語に対して、訓練フェースの結果を参照してp(w_j, c_i)を得る

pwj_cleaner = nb_train.pwj_cleaner
pwj_mp3player = nb_train.pwj_mp3player



# ----- ----- ----- ----- ----- # 3
#　N(w_j, x)とp(w_j, c_i)の情報から分類クラスを決定する