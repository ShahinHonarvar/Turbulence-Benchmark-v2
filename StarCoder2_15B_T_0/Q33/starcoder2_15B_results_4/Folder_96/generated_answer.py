def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 77 and i < 84 and c.isalpha() and (c.lower() in 'aeiou') and (c > '(') and (c <= 'G'):
            vowels.append(c)
    return vowels