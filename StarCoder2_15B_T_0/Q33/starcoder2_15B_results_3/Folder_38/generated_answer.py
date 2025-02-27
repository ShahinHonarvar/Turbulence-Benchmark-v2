def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 17 and i < 65 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'U') and (c <= '{'):
            vowels.append(c)
    return vowels