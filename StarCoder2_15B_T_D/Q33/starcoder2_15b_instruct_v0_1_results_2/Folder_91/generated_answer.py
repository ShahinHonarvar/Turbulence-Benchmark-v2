def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 4 and i < 8 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'P') and (c <= 'r'):
            vowels.append(c)
    return vowels