def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string):
        if i >= 14 and i < 60 and (c in vowels) and (c > 'd') and (c <= 'v'):
            result.append(c)
    return result