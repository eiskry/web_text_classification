import MeCab as mc
from collections import Counter
import pandas as pd
import math

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

def idf(word):
    df = pd.read_csv("uniq_sort.csv", names = ('count', 'word'))
    df2 = df[df["word"] == word]
    df_value = df2.iloc[0]['count']
    value = 1000/df_value
    idf_value = math.log10(value) + 1
    return idf_value


text1 = open("train.cleaner.txt", "r", encoding = "utf-8")
text2 = open("train.mp3player.txt", "r", encoding = "utf-8")
text3 = open("test.txt", "r", encoding = "utf-8")

def tf_idf2(text):
    while True:
        line = text.readline()
        if line:
            # print(line)
            words = mecab_analysis(line)
            counter = Counter(words)
            i = 0
            for word, count in counter.most_common():
                if len(word) > 0:
                    i = i + 1
            for word, count in counter.most_common():
                if len(word) > 0:
                    tf = math.log10(count+1) / math.log10(i)
                    wei = tf * idf(word)
                    print("%s:%f  "%(word, wei),end ="")
            print("")
            print("")
        else:
            break
       

def main():
    tf_idf2(text1)

if __name__ == '__main__':
    main()
    