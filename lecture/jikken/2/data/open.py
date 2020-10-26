import codecs

fin  = codecs.open('test.txt', 'r', 'euc_jp')
fout = codecs.open('text3.txt', 'w', 'shift_jis')

for line in fin:
    fout.write(line)