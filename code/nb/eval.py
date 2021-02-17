# eval.py

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--a_file', action="store", type=argparse.FileType('r'), required=True )
parser.add_argument('-b', '--b_file', action="store", type=argparse.FileType('r'), required=True )

args = parser.parse_args()

# ----- ----- ----- ----- -----
fpb = args.b_file

cc = 0; cm = 0; mc = 0; mm = 0; z = 0
all = 0

for label_ans in args.a_file:
  label_ans = label_ans.rstrip()

  label_out = fpb.readline()
  label_out = label_out.rstrip()

  if label_ans == 'cleaner' and label_out == 'cleaner':
    cc += 1
  elif label_ans == 'cleaner' and label_out == 'mp3player':
    cm += 1
  elif label_ans == 'mp3player' and label_out == 'cleaner':
    mc += 1
  elif label_ans == 'mp3player' and label_out == 'mp3player':
    mm += 1
  else:
    z += 1

  all += 1

print( float( cc + mm ) / float( all ) )
print('cc:' + str(cc) + ' cm:' + str(cm) + ' mc:' + str(mc) + ' mm:' + str(mm) )

# ----- ----- ----- ----- -----
