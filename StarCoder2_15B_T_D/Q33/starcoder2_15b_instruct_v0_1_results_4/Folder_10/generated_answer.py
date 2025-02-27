def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 31 and i < 37 and (c in 'aeiou') and (c > ';') and (c <= 't'):
            vowels.append(c)
    return vowels