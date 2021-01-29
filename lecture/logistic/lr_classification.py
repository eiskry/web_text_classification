import ast
import math
import my_function

##### 分類ステップ
##### 入力文書xに対して、分類クラスを決定する


# def decide_class(test_data, w):
#     output_class = {}
#     tid = 1
#     for id in test_data.keys():
#         val_class = 0
#         for val in test_data[id].keys():
#             if (val not in w):
#                 tmp = 0
#             else:
#                 tmp = test_data[id][val]* w[val]
#             val_class = val_class + tmp
#         val_class = my_function.logi_sig(val_class)
#         output_class_ = 'pos' if val_class >= 0.5 else 'neg'
#         output_class[tid] = output_class_
#         tid += 1
#     return output_class

def decide_class(test_data, w_pos, w_neg):
    output_class = {}
    tid = 1
    for id in test_data.keys():
        # pos識別
        val_class_pos = 0
        for val in test_data[id].keys():
            if (val not in w_pos):
                tmp = 0
            else:
                tmp = test_data[id][val] * w_pos[val]
            val_class_pos = val_class_pos + tmp
        # neg識別
        val_class_neg = 0
        for val in test_data[id].keys():
            if (val not in w_neg):
                tmp = 0
            else:
                tmp = test_data[id][val] * w_neg[val]
            val_class_neg = val_class_neg + tmp
        val_class_ = my_function.logi_sig(val_class_pos) - my_function.logi_sig(val_class_neg)
        output_class_ = 'pos' if val_class_ >= 0.5 else 'neg'
        output_class[tid] = output_class_
        tid += 1
    return output_class