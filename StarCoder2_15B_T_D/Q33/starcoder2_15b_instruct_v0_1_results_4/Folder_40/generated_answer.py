def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 2 and i < 7 and (c in 'aeiou') and (c > '^') and (c <= 'd'):
            vowels.append(c)
    return vowels