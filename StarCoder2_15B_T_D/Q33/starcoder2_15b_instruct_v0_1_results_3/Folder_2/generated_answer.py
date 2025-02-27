def return_vowels(s):
    vowels = []
    for i, c in enumerate(s):
        if i >= 170 and i < 645 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'E') and (c <= '~'):
            vowels.append(c)
    return vowels