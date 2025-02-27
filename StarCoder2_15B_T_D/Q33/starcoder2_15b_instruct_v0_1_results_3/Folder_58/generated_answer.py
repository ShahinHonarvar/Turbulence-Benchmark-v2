def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 260 and i < 322 and (c in 'AEIOU') and (c > '%'):
            vowels.append(c)
    return vowels