###
def minion_games(string):
    string = string
    vowels = 'EIUOA'
    kevin = 0
    stuart = 0
    length_s = len(string)
    for i in range(length_s):
        if string[i] in vowels:
            kevin = kevin + length_s - i
        else:
            stuart = stuart + length_s-i

    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")
minion_games('BANANA')
