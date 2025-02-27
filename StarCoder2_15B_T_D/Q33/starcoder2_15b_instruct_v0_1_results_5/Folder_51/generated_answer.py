def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string):
        if i >= 56 and i < 68 and (c.lower() in vowels) and (c.lower() > 'm') and (c.lower() <= 'x'):
            result.append(c)
    return result