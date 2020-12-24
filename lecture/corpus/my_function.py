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

def change_dict_key(d, old_key, new_key):
    d[new_key] = d.pop(old_key)
    return d

def shift_keys(data, n):
    new_data = {}
    length = len(data)
    for i in range(length):
        i = i + 1
        new_data[i+n] = data[i]
    return new_data

def link_data(data1, data2):
    n = len(data1)
    # print(n)
    shifted_data2 = shift_keys(data2, n)
    data1.update(shifted_data2)
    return data1