def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 86 and i < 99 and (c in 'AEIOU') and (c > 'E') and (c <= 'r'):
            vowels.append(c)
    return vowels