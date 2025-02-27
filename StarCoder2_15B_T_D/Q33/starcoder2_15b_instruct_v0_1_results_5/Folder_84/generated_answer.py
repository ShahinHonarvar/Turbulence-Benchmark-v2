def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 770 and i < 852 and (c in 'AEIOU') and (c > 'B') and (c <= 'i'):
            vowels.append(c)
    return vowels