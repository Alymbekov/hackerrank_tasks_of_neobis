#def merge_the_tools(string, k):
 #   string = str(input('Введите строчные буквы:'))
 #  k = int(input('Введите число для разделения:'))
  #  for i in range(0,len(string),k):
        #print(i)
        #в i в начале будет 0:0 +3
        #потом 3:3 +3
        #так как в цикле плюсуется
        #и дальше по логике
   #     c = string[i:i + k]
        #print()
        #print(c)
    #    res = set(c)
     #   result = list(res)
      #  acummulator = []
       # for y in result:
        #    if y not in acummulator:
#         #       acummulator.append(y)
       # print(''.join(acummulator))

#merge_the_tools('',3)
def merge_the_tools(string, k):
    n = len(string)
    inc = k
    for i in range(0, n, inc):
        s = string[i:i + inc]
        for j in range(len(s)):
                varr = sorted(set(s), key=s.index)
                result = ''.join(varr)
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
