def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 15 and i < 86 and c.isalpha() and (c.lower() in 'aeiou') and (c > '@') and (c <= '~'):
            vowels.append(c)
    return vowels