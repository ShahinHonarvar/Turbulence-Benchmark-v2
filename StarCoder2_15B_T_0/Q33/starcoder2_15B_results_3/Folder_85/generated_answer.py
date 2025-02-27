def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 55 and i < 65 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'Z') and (c <= 'w'):
            vowels.append(c)
    return vowels