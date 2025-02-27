def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 24 and i < 68 and (c in 'aeiou') and (c > 'f') and (c <= '|'):
            vowels.append(c)
    return vowels