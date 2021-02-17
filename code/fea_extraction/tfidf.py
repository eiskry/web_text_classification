import MeCab as mc
from collections import Counter
import pandas as pd
import csv
import math
import ast

def mecab_analysis(text):
    t = mc.Tagger("-Ochasen")
    t.parse('')
    node = t.parseToNode(text)
    output = []
    while node:
        if node.surface != "":
            word_type = node.feature.split(",")[0]
            if word_type in ["形容詞","動詞","名詞","副詞","助動詞","記号","助詞"]:
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output

# ----- ----- ----- ----- ----- # 全文書の読み込み
tid = 0
# 教師文書のベクトル、クラスラベルを読み込み
space = {}
for line in open('train.cleaner.txt', 'r'):
    space[tid] = line
    tid += 1
# print(tid)
for line in open('train.mp3player.txt', 'r'):
    space[tid] = line
    tid += 1
# print(tid)

for line in open('test.txt', 'r'):
    space[tid] = line
    tid += 1
N = tid
# print(N)

# ----- ----- ----- ----- ----- # 単語wの全文書の出現頻度
with open('all_file_count.txt', 'w') as f:
    for id in space.keys():
        # 全文書の各行
        line = space[id]
        # 解析
        words = mecab_analysis(line)
        counter = Counter(words)
        for word, count in counter.most_common():
            if len(word) > 0:
                # print("%s:%d  "%(word, count),end ="")
                print("%s "%(word),end ="", file =f)
        # print("", file =f)

for line in open('all_file_count.txt', 'r'):
    words = line
    word_count = {}
    for word in words.split():
        if not word in word_count:
            word_count[word] = 0
        word_count[word] += 1

# ----- ----- ----- ----- ----- # 単語wの各文書の出現頻度
tid = 0
space_train_file = {}
for line in open('train.cleaner.txt', 'r'):
    space_train_file[tid] = line
    tid += 1
# print(tid)

with open('each_file_count.txt', 'w') as f2:
    for id in space_train_file.keys():
        line = space_train_file[id]
        # 解析
        words = mecab_analysis(line)
        counter = Counter(words)
        for word, count in counter.most_common():
            if len(word) > 0:
                # print(len(word))
                print("%s:%d "%(word, count),end ="", file =f2)
                # print("%s "%(word),end ="", file =f)

        print("", file =f2)

def str_dic(x):
    d = x.strip()
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "') + '}'
    d2 = ast.literal_eval(d1)
    return d2

tid = 0
space_train_file_dic = {}
for line in open('each_file_count.txt', 'r'):
    x = str_dic(line)
    space_train_file_dic[tid] = x
    tid += 1
# print(tid)
# print(space_train_file_dic[5]['。'])


# ----- ----- ----- ----- ----- # tfidfの計算
for id in space_train_file_dic.keys():
    dic_temp = space_train_file_dic[id]

    for id2 in space_train_file_dic[id].keys():
        df_value =  word_count[id2]
        idf_value = math.exp( N / df_value ) + 1
        tf_value= space_train_file_dic[id][id2]
        space_train_file_dic[id][id2] = tf_value * idf_value
# print(space_train_file_dic[5]['。'])

# ----- ----- ----- ----- ----- # 結果の出力

with open('result.txt', 'w') as f3:
    for id in space_train_file_dic.keys():
        dic = space_train_file_dic[id]
        line_ = str(dic)
        line = line_.replace('{', '').replace('\'', '').replace(', ', ' ').replace(': ', ':').replace('}', '')
        print(line, file = f3)
        # print("", file = f3)
        

# for line in open('pre_result.txt', 'r'):
#     line_ = line.replace('{', '').replace('\'', '').replace(', ', ' ').replace(': ', ':').replace('}', '')
#     with open('result.txt', 'w') as f4:
#         print(line_, file = f4)
    # print(line_)

# for line in open('pre_result.txt', 'r'):
#     with open('result.txt', 'w') as f4:
#         print(line, file = f4)
#     # print(line_)