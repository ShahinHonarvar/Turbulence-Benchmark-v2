def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 34 and i < 58 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'b') and (c <= 'o'):
            vowels.append(c)
    return vowels