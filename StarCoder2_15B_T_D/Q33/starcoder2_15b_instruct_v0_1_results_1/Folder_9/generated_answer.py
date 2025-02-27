def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 13 and i < 35 and (c > '8') and (c <= 'F'):
            if c in 'AEIOU':
                vowels.append(c)
    return vowels