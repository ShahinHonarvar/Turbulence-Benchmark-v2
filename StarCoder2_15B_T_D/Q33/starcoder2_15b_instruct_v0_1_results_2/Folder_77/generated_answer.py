def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 837 and i < 975 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'N') and (c <= 'W'):
            vowels.append(c)
    return vowels