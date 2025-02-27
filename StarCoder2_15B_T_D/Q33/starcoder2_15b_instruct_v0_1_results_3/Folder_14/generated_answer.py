def return_vowels(string):
    vowels = []
    for i in range(47, 61):
        if i > 9 and i <= ord('O'):
            vowels.append(string[i])
    return vowels