def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string):
        if i >= 1 and i < 7 and (c in vowels) and (c > 'f') and (c <= 'j'):
            result.append(c)
    return result