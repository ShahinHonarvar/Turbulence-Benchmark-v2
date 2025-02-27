def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if 43 <= i < 70 and c in vowels and (c > '*') and (c <= 'b'):
            result.append(c)
    return result