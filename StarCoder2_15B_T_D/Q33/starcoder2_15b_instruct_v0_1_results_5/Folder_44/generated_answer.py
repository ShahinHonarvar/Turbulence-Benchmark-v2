def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 46 and i < 49 and (c in 'aeiou') and ('[' < c <= 'p'):
            vowels.append(c)
    return vowels