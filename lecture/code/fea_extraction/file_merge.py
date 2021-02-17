import MeCab as mc
from collections import Counter
import subprocess
import csv
import pandas as pd

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

text1 = open("train.cleaner.txt", "r", encoding = "utf-8")
text2 = open("train.mp3player.txt", "r", encoding = "utf-8")
text3 = open("test.txt", "r", encoding = "utf-8")

def merge(text):
    while True:
        line = text.readline()
        if line:
            # print(line)
            words = mecab_analysis(line)
            counter = Counter(words)
            for word, count in counter.most_common():
                if len(word) > 0:
                    with open('all_file.txt', 'a') as f:
                        print("%s"%word , file=f)
        else:
            break



# def count_csv(text_):
#     words = mecab_analysis(text_)
#     counter_ = Counter(words_)
#     for word, count in counter.most_common():
#         if len(word) > 0:
#             print("%s:%d  "%(word, count), end = "")

def main():
    b1 = merge(text1)
    b2 = merge(text2)
    b3 = merge(text3)
    # text_csv_converter('uniq_sort.txt')


if __name__ == '__main__':
    main()
    