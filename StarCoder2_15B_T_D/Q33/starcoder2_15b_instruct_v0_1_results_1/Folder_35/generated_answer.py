def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 483 and i < 664 and (c in 'aeiou') and (c > '&') and (c <= 'h'):
            vowels.append(c)
    return vowels