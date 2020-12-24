import MeCab as mc
from collections import Counter
import ast
import math

# ----- ----- ----- ----- ----- # 関数の定義
# 特徴抽出結果を受け取り辞書に変換
def str_dic(x):
    d = x
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "').replace('"":"', '":"') + '}'
    d2 = ast.literal_eval(d1)
    return d2

# tf特徴抽出結果を読み込む
def read_tf(text):
    tid = 0
    space = {}
    for line in text:
        line = line.replace(" \n", "\n")
        line_ = str_dic(line)
        space[tid] = line_
        tid += 1
    return space

def partial_data(data, s, e):
    partial_data ={}
    for j in range(s, e):
        partial_data[j-s+1] = data[j]
    return partial_data

def make_split_data(data, n):
    split_data={}
    split_num = n
    data_size = len(data)
    s = 0
    for i in range(split_num):
        i = i + 1
        e = int(data_size/split_num * i)
        split_data[i-1] = partial_data(data, s, e)
        s = e
    return split_data

def shift_keys(data, n):
    new_data = {}
    for i in range(len(data)):
        new_data[n+1] = data[i]
    return new_data