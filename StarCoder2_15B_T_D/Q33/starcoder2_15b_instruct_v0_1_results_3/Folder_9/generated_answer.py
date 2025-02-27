def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if i >= 13 and i < 35 and (c in vowels) and (c > '8') and (c <= 'F'):
            result.append(c)
    return result