def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string):
        if i >= 19 and i < 32 and (c > '0') and (c <= '7'):
            result.append(c)
    return result