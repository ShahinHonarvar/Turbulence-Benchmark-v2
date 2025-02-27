def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 19 and i < 32 and (c > '0') and (c <= '7'):
            vowels.append(c)
    return vowels