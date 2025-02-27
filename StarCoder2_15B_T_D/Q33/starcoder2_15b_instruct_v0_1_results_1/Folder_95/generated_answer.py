def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 32 and i < 61 and (c in 'AEIOU') and (c > '?') and (c <= 'P'):
            vowels.append(c)
    return vowels