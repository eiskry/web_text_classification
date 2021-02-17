import subprocess

text1 = 'sample.txt'
text2 = 'sample_uniq_sort.txt'

args1 = ['LC_ALL=C', 'sort', 'sample.txt']
res1 = subprocess.check_output(args1)
with open('sample_uniq_sort.txt', mode='w') as f:
        f.write(res1)

args2 = ['uniq','-c', 'sample_uniq_sort.txt']
res2 = str(subprocess.check_output(args2))
with open('sample_uniq_sort.txt', mode='w') as f:
        f.write(res2)

args3 = ['sort', '-n', '-r', 'sample_uniq_sort.txt']
res3 = str(subprocess.check_output(args3))
with open('sample_uniq_sort.txt', mode='w') as f:
        f.write(res3)

