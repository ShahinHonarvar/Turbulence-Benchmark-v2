def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 133 and i < 306 and (c in 'aeiou') and (c > 'c') and (c <= 'd'):
            vowels.append(c)
    return vowels