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
w_t_pos = {}
w_t_neg = {}
val = {}
correct_rate = {}

for i in range(n):
    # lr
    ## 訓練ステップ    
    # 重みベクトルwを初期化する
    w_pos[i] = lr_train.w_initialize(train_pos_data[i])
    w_neg[i] = lr_train.w_initialize(train_neg_data[i])
    # w_pos[i].update(w_neg[i])
    # w[i] = w_pos[i]

    # 重みベクトルwを更新する
    for j in range(100):
        for id in train_pos_data[i].keys():
            w_t_pos[i] = {}
            w_t_pos[i] = lr_train.update_w_t(train_pos_data[i][id], w_pos[i], 1)
            w_pos[i] = lr_train.update_w(w_pos[i], w_t_pos[i])
    
    for k in range(100):
        for id in train_neg_data[i].keys():
            w_t_neg[i] = {}
            w_t_neg[i] = lr_train.update_w_t(train_neg_data[i][id], w_neg[i], 0)
            w_neg[i] = lr_train.update_w(w_neg[i], w_t_neg[i])

    ## 分類ステップ
    val[i] = lr_classification.decide_class(test_data[i], w_pos[i], w_neg[i])
    count = 0
    for k in range(len(split_pos[i])):
        if val[i][k+1] == 'pos':
            count += 1
    for l in range(len(split_pos[i]), len(test_data[i])):
        if val[i][l+1] == 'neg':
            count += 1
    correct_rate[i] = count / len(test_data[i])

# ----- ----- ----- ----- ----- # 4
# 4. 評価
print("")
print("Results")
for i in range(n):
    print(i+1 , ":",  correct_rate[i])

# 評価値の平均値を計算する.
print("Average")
sum = 0
for i in range(n):
    sum = correct_rate[i] + sum
average = sum / 5
print(average)
print("")
