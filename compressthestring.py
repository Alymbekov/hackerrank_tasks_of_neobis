x =0
#string
string = input()
while x in range(len(string)) :
    t = string[x]
    k = x+1
    c = 1
    while k<len(string) :
        if string[k] != t:
            break
        c += 1
        k += 1
    print((c,int(string[x])),end=' ')
    x = k
