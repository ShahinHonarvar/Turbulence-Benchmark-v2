def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if i >= 260 and i < 322 and (c in vowels) and (c > '%') and (c <= 'U'):
            result.append(c)
    return result