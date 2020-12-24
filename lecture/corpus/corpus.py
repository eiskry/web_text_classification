import my_function

# ----- ----- ----- ----- ----- # 1
# データセットを n 個のブロックに分割する.
n=5

# positive_tf
text = open("positive_tf.txt", "r")
pos_data = my_function.read_tf(text)

# s = 0
# for i in range(n):
#     i = i + 1
#     e = int(pos_size/n * i)
#     partial_pos[i-1] = my_function.make_partial_data(pos_data, s, e)
#     s = e

# # print(len(partial_pos))
# tmp = 0
# for i in range(n):
#     tmp = tmp + len(partial_pos[i])
#     print(len(partial_pos[i]))
# print(tmp)

# posデータを分割
split_pos = my_function.make_split_data(pos_data, n)
# tmp = 0
# for i in range(n):
#     tmp = tmp + len(split_pos[i])
#     print(len(split_pos[i]))
# print(tmp)

# negative_tf
text = open("negative_tf.txt", "r")
neg_data = my_function.read_tf(text)

split_neg = my_function.make_split_data(neg_data, n)

# print(split_pos[2])
# print(len(split_pos[0]))
# print(split_pos[2])

# for id in split_pos[2].keys:
#     print(id)


# print(len(split_pos[0])+ len(split_pos[1]))

# new_data = my_function.link_data(split_pos[0], split_pos[1])
# print(len(new_data))

# tmp = 0
# for i in range(n):
#     tmp = tmp + len(split_neg[i])
#     print(len(split_neg[i]))
# print(tmp)

# 2. ひとつのブロックを評価データ，のこりを学習データとする.
### case 1
##### test = 0


### case 2
##### test = 1

### case 3
##### test = 2

### case 4
##### test = 3

### case 5
##### test = 4


# 3. 評価データに採用するブロックを変化させながら，学習&評価を n 回繰り返す. 



# 4. さいごに，評価値の平均値を計算する.