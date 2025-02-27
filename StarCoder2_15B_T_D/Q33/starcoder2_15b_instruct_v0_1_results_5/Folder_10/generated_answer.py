def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 31 <= i < 37 and c.isalpha() and (c.lower() in 'aeiou') and (c > ';') and (c <= 't'):
            vowels.append(c)
    return vowels