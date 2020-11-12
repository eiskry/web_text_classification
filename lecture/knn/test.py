d = {'key1': 1, 'key2': 2, 'key3': 3}
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


input = read_input_vec(d)
print(input)

def read_vec(x, label):
    x_vector = Vec(x, label)
    return x_vector

tid = 0
# 教師文書のベクトル、クラスラベルを読み込み
space = {}
space[tid] = read_vec( d, 'cleaner')

print(space)