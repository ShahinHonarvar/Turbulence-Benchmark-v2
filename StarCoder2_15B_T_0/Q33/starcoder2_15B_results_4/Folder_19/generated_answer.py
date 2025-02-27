def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 51 and i < 77 and (c > '4') and (c <= '=') and (c in 'aeiou'):
            vowels.append(c)
    return vowels