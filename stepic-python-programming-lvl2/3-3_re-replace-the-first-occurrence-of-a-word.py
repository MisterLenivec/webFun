# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a"
# (регистр не важен), на слово "argh".

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\ba+\b', 'argh', line, flags=re.IGNORECASE, count=1))
