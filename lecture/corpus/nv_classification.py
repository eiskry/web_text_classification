import ast
import math
import my_function

##### 分類ステップ
##### 入力文書xに対して、分類クラスを決定する

# ----- ----- ----- ----- ----- # 1
# 入力文書の各単語に対して、N(w_j, x)を求める



# ----- ----- ----- ----- ----- # 2
# 入力文書の各単語に対して、訓練フェースの結果を参照してp(w_j, c_i)を得る

# あるクラスに関してP(wj|ci) を求める
def pwj_class(test_data, pwj_class, all_words_class):
    for id in test_data.keys():
        for val in test_data[id].keys():
            if (val not in pwj_class):
                pwj_class[val] = 1 / all_words_class
    return pwj_class

# ----- ----- ----- ----- ----- # 3
#　N(w_j, x)とp(w_j, c_i)の情報から分類クラスを決定する

def decide_class(test_data, pwj_class1, pwj_class2):
    val = {}
    for id in test.keys():
        val_class1 = 0
        val_class2 = 0
        for val in test_data[id].keys():
            tmp = test_data[id][val]* math.log(pwj_class1[val])
            val_class1 = val_class1 + tmp
        for val in test_data[id].keys():
            tmp = test_data[id][val]* math.log(pwj_class2[val])
            val_class2 = val_class2 + tmp
        output_class = 'pos' if val_cleaner > val_mp3player else 'neg'
        val[id] = output_class
    return val