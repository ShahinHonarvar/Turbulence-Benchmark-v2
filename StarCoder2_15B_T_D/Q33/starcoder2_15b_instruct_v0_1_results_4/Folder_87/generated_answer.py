def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(str):
        if i >= 34 and i < 58 and (c in vowels) and (c > 'b') and (c <= 'o'):
            result.append(c)
    return result