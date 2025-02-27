def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 149 <= i < 313 and c.isalpha() and (c.lower() in 'abcdefghijklmnopqrstuvwxyz') and (c.lower() > 'm') and (c.lower() <= 'j'):
            vowels.append(c)
    return vowels