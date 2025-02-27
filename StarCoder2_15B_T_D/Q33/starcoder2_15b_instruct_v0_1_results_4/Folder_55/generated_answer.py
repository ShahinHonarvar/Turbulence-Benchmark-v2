def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string):
        if i >= 1 and i < 5 and (c in vowels) and (c > '!') and (c <= 'j'):
            result.append(c)
    return result