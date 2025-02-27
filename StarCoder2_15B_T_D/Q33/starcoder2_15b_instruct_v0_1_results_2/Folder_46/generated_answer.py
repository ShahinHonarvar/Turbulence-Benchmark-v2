def return_vowels(string):
    vowels = 'aeiou'
    result = ''
    for i, c in enumerate(string):
        if i >= 10 and i < 83 and (c in vowels) and (c > '%') and (c <= 'e'):
            result += c
    return result