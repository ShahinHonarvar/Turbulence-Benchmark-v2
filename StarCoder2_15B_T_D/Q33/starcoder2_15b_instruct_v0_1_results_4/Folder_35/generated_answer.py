def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string):
        if 483 <= i < 664 and c in vowels and (c > '&') and (c <= 'h'):
            result.append(c)
    return result