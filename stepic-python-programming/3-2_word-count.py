# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке
# число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.

a = input().lower().split()
s = set(a)
for x in s:
    print(x + ' ' + str(a.count(x)))
