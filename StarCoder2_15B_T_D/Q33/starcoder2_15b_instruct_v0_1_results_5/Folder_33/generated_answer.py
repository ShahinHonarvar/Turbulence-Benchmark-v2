def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 163 and i < 771 and (c in 'AEIOU'):
            vowels.append(c)
    return vowels