def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 36 and i < 56 and c.isalpha() and (c.lower() in 'aeiou'):
            if '+' < c <= '/':
                vowels.append(c)
    return vowels