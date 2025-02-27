def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if c in ['a', 'e', 'i', 'o', 'u'] and 34 <= i < 58 and (c > 'b') and (c <= 'o'):
            vowels.append(c)
    return vowels