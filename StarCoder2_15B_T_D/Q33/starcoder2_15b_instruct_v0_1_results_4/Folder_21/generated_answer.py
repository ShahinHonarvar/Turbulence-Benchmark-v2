def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 464 and i < 574 and c.isalpha() and (c.lower() > 'a') and (c.lower() <= 'g'):
            vowels.append(c)
    return vowels