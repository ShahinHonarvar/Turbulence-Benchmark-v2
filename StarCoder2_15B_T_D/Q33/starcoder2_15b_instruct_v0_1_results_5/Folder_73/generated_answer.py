def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if i >= 47 and i < 89 and (c in vowels) and (c > '@') and (c <= 'n'):
            result.append(c)
    return result