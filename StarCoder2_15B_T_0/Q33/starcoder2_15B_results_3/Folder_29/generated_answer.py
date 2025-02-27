def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 19 and i < 20 and c.isalpha() and (c.lower() in 'aeiou') and (c > '<') and (c <= 'p'):
            vowels.append(c)
    return vowels