def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 36 <= i < 56 and c.isalpha() and (c.lower() in 'aeiou') and ('+' < c <= '/'):
            vowels.append(c)
    return vowels