import subprocess
args = ['cat', 'all_file2.txt']
res = subprocess.call(args)
#=> lsコマンドの結果
print(res)
#=> コマンドが成功していれば 0