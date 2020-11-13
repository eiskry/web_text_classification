import ast
d = "母親:9.96578428466209 ・:9.30479442002342 住ん:8.96578428466209 母:8.38082178394093 送り:8.38082178394093 くらい:8.09384209477498 メンテナンス:7.96578428466209 失敗:7.38082178394093 プレゼント:7.05889368905357 」:7.04568157762672 「:7.02914634565952 取れる:6.96578428466209 清掃:6.79585928321977 気持ち:6.50635266602479 ！:6.26578854099469 ほこり:6.05889368905357 こんな:6.05889368905357 まし:5.5874894287502 綺麗:5.50635266602479 楽:5.47393118833241 みる:5.41119543298445 の:5.39281834596851 日:5.265344566521 安い:5.18442457113743 ）:5.02091412871505 （:5.02091412871505 良く:4.96578428466209 し:4.95826450131955 た:4.89726919304376 大:4.68038206579984 価格:4.45798964446339 部屋:4.39592867633114 って:4.35107444054688 ゴミ:3.7178567712185 満足:3.67116353577046 で:3.58288444548447 、:3.35148403269825 に:3.30944078130988 が:3.17668106716071 。:3.14076314216248 なり:3.05889368905357 や:2.94341647163363 使っ:2.90508835297453 機:2.88363524330822 いい:2.8059129478837 購入:2.62593428177746 も:2.58318403303281 掃除:2.50635266602479 だ:2.44222232860507 から:2.42662547355406 て:2.2218318028037 か:2.14241704461585 と:1.28806464302108"
# d1 = '{' + '\'' + d.replace(':', '":').replace(' ', ', \'') + '}'
# d2 = ast.literal_eval(d1)
# print(d2)

def str_dic(x):
    d = x
    d1 = '{' + '"' + d.replace(':', '":').replace(' ', ', "') + '}'
    d2 = ast.literal_eval(d1)
    return d2

d1= str_dic(d)
print(d1)
print(d1['母親'])

d2 = {"key1": 4, "key3": 5, "key5": 6}
# print(d2)