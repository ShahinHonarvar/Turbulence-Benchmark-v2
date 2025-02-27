def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if 56 <= i < 96 and c in vowels and ('&' < c <= 'T'):
            result.append(c)
    return result