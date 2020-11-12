import ast
d = "key1:1 key2:2 key3:3"
# d1 = '{' + '\'' + d.replace(':', '":').replace(' ', ', \'') + '}'
# d2 = ast.literal_eval(d1)
# print(d2)

def str_dic(x):
    # d1 = '{' + '"' + d.replace(':', '":"').replace(' ', '", "') + '"}'
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "') + '}'
    d2 = ast.literal_eval(d1)
    return d2

d1= str_dic(d)
print(d1)
print(d1['key1']+d1['key2'])

d2 = {"key1": 4, "key3": 5, "key5": 6}
print(d2)