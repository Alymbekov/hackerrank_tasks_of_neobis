from itertools import combinations
k = int(input('Введите k:'))
l = input('введите l').split()
C = list(combinations(l, k))
f = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(f))/len(C)))
