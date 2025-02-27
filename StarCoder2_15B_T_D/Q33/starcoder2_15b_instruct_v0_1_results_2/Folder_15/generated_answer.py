def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 5 and i < 6 and (c > '3') and (c <= '^'):
            vowels.append(c)
    return vowels