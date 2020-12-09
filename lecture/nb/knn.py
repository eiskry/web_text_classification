import sys
import argparse
import math
import ast

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--a_file', action="store", type=argparse.FileType('r'), required=True )
parser.add_argument('-b', '--b_file', action="store", type=argparse.FileType('r'), required=True )
parser.add_argument('-k', '--k_int', action="store", type=int, required=True )

args = parser.parse_args()

k = args.k_int
# ----- ----- ----- ----- -----
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
tid = 0
# 教師文書のベクトル、クラスラベルを読み込み
space = {}
for line in open('train.cleaner.vec=tfidf.txt', 'r'):
    line_ = str_dic(line)
    space[tid] = read_vec( line_, 'cleaner')
    tid += 1

for line in open('train.mp3player.vec=tfidf.txt', 'r'):
    line_ = str_dic(line)
    space[tid] = read_vec( line_, 'mp3player')
    tid += 1

# ----- ----- ----- ----- ----- # 入力文書に対する処理
# 標準入力
for x in sys.stdin:
    # 入力文書の読み込み
    input = read_input_vec( x )
    # 類似度計算
    s = {}
    # 教師文書の辞書のキーについて計算
    for id in space.keys():
        # 教師文書のベクトル
        v = space[id].x
        s[id] = sim( input, v )

    # 近傍文書の獲得
    class_a_count = 0
    count = 0
    for id,tmp in sorted( s.items(), key=lambda x: x[1], reverse=True):
        if( count >= k ): break
        if( space[id].c == 'cleaner' ): class_a_count += 1
        count += 1

    # 意思決定
    output_class = 'cleaner' if class_a_count * 2 > k else 'mp3player'
    print( output_class )
# ----- ----- ----- ----- -----