def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if i >= 163 and i < 771 and (c in vowels) and (c > ':') and (c <= 'E'):
            result.append(c)
    return result