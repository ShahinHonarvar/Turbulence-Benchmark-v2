def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if i >= 70 and i < 76 and (c in vowels) and (c > '2') and (c <= ':'):
            result.append(c)
    return result