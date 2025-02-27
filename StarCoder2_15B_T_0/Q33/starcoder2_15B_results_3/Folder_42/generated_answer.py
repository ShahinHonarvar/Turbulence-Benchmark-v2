def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 12 and i < 39 and (c in 'aeiou') and (c > ';') and (c <= '|'):
            vowels.append(c)
    return vowels