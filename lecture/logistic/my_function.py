import ast
import math

num_split = 5

# ----- ----- ----- ----- ----- # 
# 特徴抽出結果を受け取り辞書に変換
def str_dic(x):
    d = x
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "').replace('"":"', '":"') + '}'
    d2 = ast.literal_eval(d1)
    return d2

# ----- ----- ----- ----- ----- # 
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

# ----- ----- ----- ----- ----- # 
# sからeまでのdataを抽出する
def partial_data(data, s, e):
    partial_data ={}
    for j in range(s, e):
        partial_data[j-s+1] = data[j]
    return partial_data

# dataをn分割する
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

# ----- ----- ----- ----- ----- # 
# 辞書のキーを変更する
def change_dict_key(d, old_key, new_key):
    d[new_key] = d.pop(old_key)
    return d

# 辞書のキーをnだけずらす
def shift_keys(data, n):
    new_data = {}
    length = len(data)
    for i in range(length):
        i = i + 1
        new_data[i+n] = data[i]
    return new_data

# 辞書型の2つのデータを結合する
def link_data(data1, data2):
    linked_data = {}
    n = len(data1)
    # print(n)
    shifted_data2 = shift_keys(data2, n)
    linked_data.update(data1)
    linked_data.update(shifted_data2)
    return linked_data

# ----- ----- ----- ----- ----- # 
# 数字の循環
def rec_num(n):
    if n > num_split - 1:
        return n - num_split
    elif n < 0:
        return n + num_split
    else:
        return n

# ----- ----- ----- ----- ----- # 
# ロジスティックシグモイド関数
def logi_sig(a):
    value = 1 / (1+(math.exp(-a)))
    return value 