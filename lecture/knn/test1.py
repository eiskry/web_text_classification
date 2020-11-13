import math
d = {'key1': 1, 'key2': 2, 'key3': 3}
d2 = {'key1': 4, 'key3': 5, 'key5': 6}
# print(d['key1'])
tid = 0
# 教師文書のベクトル、クラスラベルを読み込み
space = {}
for w in d:
    space[tid] = w
    tid += 1

class Vec():
    # def __init__(self, c , magnitude):
    def __init__(self, x, c ):
        self.x = x
        self.c = c
        # self.magnitude = magnitude

def read_input_vec(x):
    x_vector = list(x.values())
    return x_vector


# input = read_input_vec(d)
# print(input)

def read_vec(x, label):
    x_vector = Vec(x, label)
    return x_vector

tid = 0
# 教師文書のベクトル、クラスラベルを読み込み
space = {}
space[1]= read_vec( d, 'cleaner')
space[2]= read_vec( d2, 'test')

print(space[1].x)
print(space[2].x)

# 類似度を計算する
def sim(x1, x2):
    sum = 0
    for kye in x1.keys():
        if (kye in x2):
            sum += x1[kye]*x2[kye]
    v1_ = 0
    for value in x1.values():
        v1_ += value*value
    v1 = math.sqrt(v1_)
    v2_ = 0
    for value in x2.values():
        v2_ += value*value
    v2 = math.sqrt(v2_)
    return sum/(v1*v2)

print(sim(d,d2))
