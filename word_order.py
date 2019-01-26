#its note

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
varr = OrderedCounter(input() for _ in range(int(input())))
print(len(varr))
print(*varr.values())
