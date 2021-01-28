import my_function
import lr_train
import lr_classification

# ----- ----- ----- ----- ----- # 1
# データセットを n 個のブロックに分割する.
n=5

# positive_tf
text = open("positive_tf.txt", "r")
pos_data = my_function.read_tf(text)
# posデータを分割
split_pos = my_function.make_split_data(pos_data, n)


# negative_tf
text = open("negative_tf.txt", "r")
neg_data = my_function.read_tf(text)
# negデータを分割
split_neg = my_function.make_split_data(neg_data, n)

# ----- ----- ----- ----- ----- # 2
# 2. ひとつのブロックを評価データ，のこりを学習データとする.
### 評価データの作成
test_data = {}
for i in range(n):
    test_data[i] = my_function.link_data(split_pos[i], split_neg[i])

# ### 学習データの作成
train_pos_data = {}
train_neg_data = {}
for i in range(n):
    tmp_pos1 = tmp_pos2 = tmp_neg1 = tmp_neg2 = {}
    ### posデータ
    tmp_pos1 = my_function.link_data(split_pos[my_function.rec_num(i-1)], split_pos[my_function.rec_num(i+1)])
    tmp_pos2 = my_function.link_data(split_pos[my_function.rec_num(i+2)], split_pos[my_function.rec_num(i+3)])
    train_pos_data[i] = my_function.link_data(tmp_pos1, tmp_pos2)

    ### negデータ
    tmp_neg1 = my_function.link_data(split_neg[my_function.rec_num(i-1)], split_neg[my_function.rec_num(i+1)])
    tmp_neg2 = my_function.link_data(split_neg[my_function.rec_num(i+2)], split_neg[my_function.rec_num(i+3)])
    train_neg_data[i] = my_function.link_data(tmp_neg1, tmp_neg2)

# ----- ----- ----- ----- ----- # 3
# 3. 評価データに採用するブロックを変化させながら，学習&評価を n 回繰り返す. 
w_pos = {}
w_neg = {}
val = {}
correct_rate = {}

for i in range(n):
    # lr
    ## 訓練ステップ
    len_pos = len(train_pos_data[i])
    len_neg = len(train_neg_data[i])
    len_total = len_pos + len_neg

    for j in range(len_total):
        c = 1 if j <= len_pos else c = 0
        w_pos[i] = lr_train.w_initialize(train_pos_data[i])
        w_neg[i] = lr_train.w_initialize(train_neg_data[i])
        w[i] = my_function.link_data(w_pos[i], w_neg[i])

        
    ### pos データについて
    w_pos[i] = lr_train.w_initialize(train_pos_data[i])
    w_pos[i] = lr_train.updata_w(train_pos_data[i], w_pos[i], 1)

    ### neg　データについて
    pwj_neg[i] = nv_train.train_count_pwj(train_neg_data[0])
    all_words_neg_class[i] = nv_train.train_count_word(pwj_neg[i])
    pwj_neg[i] = nv_train.train_pwj_class(pwj_neg[i], all_words_neg_class[i])

    ## 分類フェーズ
    # nwjx[i] = test_data[i]
    pwj_pos[i] = nv_classification.pwj_class(test_data[i], pwj_pos[i], all_words_pos_class[i])
    pwj_neg[i] = nv_classification.pwj_class(test_data[i], pwj_neg[i], all_words_neg_class[i])
    val[i] = nv_classification.decide_class(test_data[i], pwj_pos[i], pwj_neg[i])
    count = 0
    for k in range(len(split_pos[i])):
        if val[i][k+1] == 'pos':
            count += 1
    for l in range(len(split_pos[i]), len(test_data[i])):
        if val[i][l+1] == 'neg':
            count += 1
    correct_rate[i] = count / len(test_data[i])

print("")
print("Results")
for i in range(n):
    print(i+1 , ":",  correct_rate[i])

# 4. さいごに，評価値の平均値を計算する.
# print("")
print("Average")
sum = 0
for i in range(n):
    sum = correct_rate[i] + sum
average = sum / 5
print(average)
print("")
