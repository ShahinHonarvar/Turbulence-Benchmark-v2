def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 22 and i < 82 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'N') and (c <= 'o'):
            vowels.append(c)
    return vowels