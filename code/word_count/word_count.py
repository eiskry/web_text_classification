import MeCab as mc
from collections import Counter

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

def count(text):
    words = mecab_analysis(text)
    counter = Counter(words)
    for word, count in counter.most_common():
        if len(word) > 0:
            print("%s:%d  "%(word, count), end = "")

def main():
    count(text1)

if __name__ == '__main__':
    main()
    