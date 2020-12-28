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

def tf(text):
    while True:
        line = text.readline()
        line = line.replace('"', '')
        if line:
            words = mecab_analysis(line)
            counter = Counter(words)
            for word, count in counter.most_common():
                if len(word) > 0:
                    print("%s:%d "%(word, count),end ="")
            print("")
        else:
            break
       

text = open("train.cleaner.txt", "r", encoding = "utf-8")

def main():
    tf(text3)

if __name__ == '__main__':
    main()
    