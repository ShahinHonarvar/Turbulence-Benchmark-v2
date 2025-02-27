def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if i >= 40 and i < 94 and (c in vowels) and (c > '4') and (c <= 'H'):
            result.append(c)
    return result