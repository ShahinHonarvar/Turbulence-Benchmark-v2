def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 45 and i < 76 and (c in 'aeiou') and (c > 'b') and (c <= 'z'):
            vowels.append(c)
    return vowels