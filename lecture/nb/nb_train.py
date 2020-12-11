import MeCab as mc
from collections import Counter
import ast

##### 訓練ステップ
##### 教師文書を利用して、各クラス、各単語についてp(w_j, c_i)を求める

# ----- ----- ----- ----- ----- # 関数・deltaの定義
# 特徴抽出結果を受け取り辞書に変換
def str_dic(x):
    d = x
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "') + '}'
    d2 = ast.literal_eval(d1)
    return d2

# smoothing　有効
delta = 1

# smoothing を行わない場合
# delta = 0

# ----- ----- ----- # cleanerクラスについてP(wj|ci)を求める
# 教師文書を読み込み
tid = 0
space = {}
for line in open('train.cleaner_tf.txt', 'r'):
    line = line.replace(" \n", "\n")
    line_ = str_dic(line)
    space[tid] = line_
    tid += 1

# 各単語の生起頻度を登録
pwj_cleaner = {}
for id in space.keys():
    for val in space[id].keys():
        if (val not in pwj_cleaner):
            pwj_cleaner[val] = space[id][val]
        else:
            pwj_cleaner[val] = pwj_cleaner[val]+space[id][val]

# cleanerクラスの全単語数を計算
all_words_cleaner = 0
for id in pwj_cleaner.keys():
    tmp = pwj_cleaner[id] + delta
    all_words_cleaner = all_words_cleaner + tmp

# 最終的なP(wj|ci)を計算
for id in pwj_cleaner.keys():
    tmp = pwj_cleaner[id] + delta
    pwj_cleaner[id] = tmp / all_words_cleaner

# P(wj|ci)をファイルに出力
with open('pwj_cleaner.txt', 'w') as f:
  print(pwj_cleaner, file=f)


# ----- ----- ----- # # mp3playerクラスについてP(wj|ci)を求める
# 教師文書を読み込み
tid = 0
space = {}
for line in open('train.mp3player_tf.txt', 'r'):
    line = line.replace(" \n", "\n")
    line_ = str_dic(line)
    space[tid] = line_
    tid += 1

# 各単語の生起頻度を登録
pwj_mp3player = {}
for id in space.keys():
    for val in space[id].keys():
        if (val not in pwj_mp3player):
            pwj_mp3player[val] = space[id][val]
        else:
            pwj_mp3player[val] = pwj_mp3player[val]+space[id][val]

# mp3playerクラスの全単語数を計算
all_words_mp3player = 0
for id in pwj_mp3player.keys():
    tmp = pwj_mp3player[id] + delta
    all_words_mp3player = all_words_mp3player + tmp

# 最終的なP(wj|ci)を計算
for id in pwj_mp3player.keys():
    tmp = pwj_mp3player[id] + delta
    pwj_mp3player[id] = tmp / all_words_mp3player

# P(wj|ci)をファイルに出力
with open('pwj_mp3player.txt', 'w') as f:
  print(pwj_mp3player, file=f)