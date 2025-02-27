def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string):
        if i >= 71 and i < 81 and c.isalpha() and (c.lower() > 'a') and (c.lower() <= 'u'):
            result.append(c)
    return result