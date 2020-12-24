import my_function

# ----- ----- ----- ----- ----- # 1
# データセットを n 個のブロックに分割する.
n=5

# positive_tf
text = open("positive_tf.txt", "r")
pos_data = my_function.read_tf(text)
pos_size = len(pos_data)

partial_pos={}
s = 0
for i in size(n):
    e = pos_size()
    for j in range(s, e):


# negative_tf
text = open("negative_tf.txt", "r")
neg_data = my_function.read_tf(text)
neg_size = len(neg_data)


# 2. ひとつのブロックを評価データ，のこりを学習データとする.



# 3. 評価データに採用するブロックを変化させながら，学習&評価を n 回繰り返す. 

# 4. さいごに，評価値の平均値を計算する.