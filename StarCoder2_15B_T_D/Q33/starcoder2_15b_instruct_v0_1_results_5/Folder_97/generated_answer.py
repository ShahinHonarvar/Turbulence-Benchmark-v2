def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 328 <= i < 455 and c.isalpha() and (c.lower() in 'aeiou') and ('a' < c.lower() <= 'z'):
            vowels.append(c)
    return vowels