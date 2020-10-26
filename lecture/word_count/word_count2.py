import subprocess
args1 = ['mecab', 'sample1.txt']

res1 = subprocess.check_output(args1)

# print res1

print("\n")
print("----------")
print("\n")

with open('analysis1.txt', mode='w') as f:
    f.write(res1)

args2 = ['sort', 'analysis1.txt']
res2 = subprocess.check_output(args2)
with open('analysis1.txt', mode='w') as f:
    f.write(res2)


args3 = ['uniq','-c', 'analysis1.txt']
res3 = subprocess.check_output(args3)
with open('analysis1.txt', mode='w') as f:
    f.write(res3)

args4 = ['sort', '-n', '-r','analysis1.txt']
res4 = subprocess.check_output(args4)
with open('analysis1.txt', mode='w') as f:
    f.write(res4)

print(res4)