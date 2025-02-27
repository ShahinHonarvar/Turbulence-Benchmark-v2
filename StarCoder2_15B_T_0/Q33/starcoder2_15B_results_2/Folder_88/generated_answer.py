def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 70 and i < 76 and (c > '2') and (c <= ':'):
            vowels.append(c)
    return vowels