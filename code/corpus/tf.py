import MeCab as mc
from collections import Counter
import sys
import fileinput
from pathlib import Path

def mecab_analysis(text):
    t = mc.Tagger("-Ochasen")
    t.parse('')
    node = t.parseToNode(text)
    output = []
    while node:
        if node.surface != "":
            word_type = node.feature.split(",")[0]
            if word_type in ["形容詞","動詞","名詞","副詞","助動詞","記号","助詞"]:
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output

if Path(sys.argv[1]).exists():  
    for line in fileinput.input():  
        if line:
            line = line.replace('"', '')
            line = line.replace('\\', '')
            words = mecab_analysis(line)
            counter = Counter(words)
            for word, count in counter.most_common():
                if len(word) > 0:
                    print("%s:%d "%(word, count),end ="")
            print("")
        else:
            break