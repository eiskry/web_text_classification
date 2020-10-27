import pandas as pd
import math
def idf(word):
    df = pd.read_csv("uniq_sort.csv", names = ('count', 'word'))
    df2 = df[df["word"] == word]
    print(".")
    df_value = df2.iloc[0]['count']
    print(df_value)
    value = 1000/df_value
    print(value)
    # idf_value = 1000/df_value
    # idf_value = math.log(value) + 1
    idf_value = math.log10(value) + 1
    
    # return idf_value
    print(idf_value)

def main():
    idf("の")


if __name__ == '__main__':
    main()
    