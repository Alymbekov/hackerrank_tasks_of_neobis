def merge_the_tools(string, k):
    string = str(input('Введите строчные буквы:'))
    k = int(input('Введите число для разделения:'))
    for i in range(0,len(string),k):
        #print(i)
        #в i в начале будет 0:0 +3
        #потом 3:3 +3
        #так как в цикле плюсуется
        #и дальше по логике
        c = string[i:i + k]
        #print()
        #print(c)
        res = set(c)
        result = list(res)
        acummulator = []
        for y in result:
            if y not in acummulator:
                acummulator.append(y)
        print(''.join(acummulator))

merge_the_tools('',3)