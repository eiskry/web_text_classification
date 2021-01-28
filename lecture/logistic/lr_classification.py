import ast
import math
import my_function

##### 分類ステップ
##### 入力文書xに対して、分類クラスを決定する


def decide_class(test_data, w):
    output_class = {}
    tid = 1
    for id in test_data.keys():
        val_class = 0
        for val in test_data[id].keys():
            tmp = test_data[id][val]* w[val]
            val_class = val_class + tmp
        output_class_ = 'pos' if val_class >= 0.5 else 'neg'
        output_class[tid] = output_class_
        tid += 1
    return output_class