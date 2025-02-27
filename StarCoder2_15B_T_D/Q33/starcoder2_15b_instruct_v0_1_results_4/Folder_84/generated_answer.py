def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 770 <= i < 852 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'B') and (c <= 'i'):
            vowels.append(c)
    return vowels