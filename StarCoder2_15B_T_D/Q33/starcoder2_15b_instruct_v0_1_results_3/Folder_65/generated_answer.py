def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if i >= 71 and i < 88 and (c > '9') and (c <= 'P') and (c in vowels):
            result.append(c)
    return result