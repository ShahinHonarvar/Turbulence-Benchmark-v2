def return_vowels(string):
    vowels = []
    for i in range(51, 77):
        if i > 4 and i <= ord('='):
            vowels.append(string[i])
    return vowels