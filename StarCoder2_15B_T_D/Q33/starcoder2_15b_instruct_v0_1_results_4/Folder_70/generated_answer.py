def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 171 and i < 402 and (c in 'aeiou') and (c > 'I') and (c <= 'k'):
            vowels.append(c)
    return vowels