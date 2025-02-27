def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string):
        if i >= 44 and i < 95 and (c > '5') and (c <= '<') and (c in vowels):
            result.append(c)
    return result