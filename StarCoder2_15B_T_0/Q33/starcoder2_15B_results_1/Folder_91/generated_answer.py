def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 4 and i < 8 and (c.lower() in 'aeiou') and ('p' < c.lower() <= 'r'):
            vowels.append(c)
    return vowels