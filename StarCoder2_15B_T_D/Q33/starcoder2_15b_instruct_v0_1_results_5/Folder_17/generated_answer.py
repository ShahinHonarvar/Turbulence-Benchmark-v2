def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 60 and i < 99 and (c in 'aeiou') and ('j' < c <= 'n'):
            vowels.append(c)
    return vowels