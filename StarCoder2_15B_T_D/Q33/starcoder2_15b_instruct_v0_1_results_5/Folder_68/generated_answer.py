def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i > 0 and i < 9 and c.isalpha() and (c.lower() in 'aeiou') and (c > '?') and (c <= 'k'):
            vowels.append(c)
    return vowels