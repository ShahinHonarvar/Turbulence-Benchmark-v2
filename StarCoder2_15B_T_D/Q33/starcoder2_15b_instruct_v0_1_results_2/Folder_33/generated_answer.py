def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 163 and i < 771 and (c > ':') and (c <= 'E'):
            vowels.append(c)
    return vowels