import math
AB = float(input('Введите длину стороны:'))
BC = float(input('Ввелите длину стороны:'))
#ugol
print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')
