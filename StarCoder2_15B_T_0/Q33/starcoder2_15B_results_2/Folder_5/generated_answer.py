def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 44 and i < 95 and (c in 'aeiou') and (c > '5') and (c <= '<'):
            vowels.append(c)
    return vowels