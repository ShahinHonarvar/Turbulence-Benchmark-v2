def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string[14:60]):
        if c.lower() in vowels and c.lower() > 'd' and (c.lower() <= 'v'):
            result.append(c)
    return result