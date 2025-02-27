def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 170 and i < 645 and (c in 'AEIOU') and (c > 'E') and (c <= '~'):
            vowels.append(c)
    return vowels