def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if i >= 17 and i < 65 and (c in vowels) and (c > 'u') and (c <= '{'):
            result.append(c)
    return result