import MeCab as mc
from collections import Counter
import ast
import math


d = {"・":3, """:2, "設備":1, "に関して":1, "風呂":1, "が":1, ",":1, "綺麗":1, "だ":1, "し":1, "景色":1, "も":1, "よく":1, "て":1, "気持ちよかっ":1, "た":1, "です":1, "★":1
}