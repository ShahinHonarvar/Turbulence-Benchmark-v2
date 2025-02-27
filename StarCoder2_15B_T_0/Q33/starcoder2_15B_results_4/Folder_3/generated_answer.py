def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 50 and i < 77 and c.isalpha() and (c.lower() in 'aeiou') and (c > '#') and (c <= 'r'):
            vowels.append(c)
    return vowels