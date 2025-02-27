def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 44 and i < 95 and c.isalpha() and (c.lower() in 'aeiou'):
            if ord(c) > 5 and ord(c) <= ord('<'):
                vowels.append(c)
    return vowels