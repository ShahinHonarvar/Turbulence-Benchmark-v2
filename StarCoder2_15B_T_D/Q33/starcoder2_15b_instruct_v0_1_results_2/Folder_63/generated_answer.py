def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 34 <= i < 69 and c.isalpha() and (c.lower() in 'aeiou') and (c > '_') and (c <= 'o'):
            vowels.append(c)
    return vowels