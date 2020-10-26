import codecs

fin  = codecs.open('train.cleaner.txt', 'r', 'euc_jp')
fout = codecs.open('text1.txt', 'w', 'shift_jis')

for line in fin:
    fout.write(line)