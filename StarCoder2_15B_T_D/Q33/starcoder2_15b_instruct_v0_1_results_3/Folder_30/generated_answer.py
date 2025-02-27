def return_vowels(string):
    vowels = 'AEIOU'
    result = []
    for i, c in enumerate(string):
        if 11 <= i < 61 and c in vowels and ('M' < c <= 'W'):
            result.append(c)
    return result