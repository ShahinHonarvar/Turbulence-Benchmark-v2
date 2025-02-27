def return_vowels(s):
    vowels = 'aeiou'
    result = ''
    for i, c in enumerate(s):
        if i >= 20 and i < 43 and (c in vowels) and (c > '5') and (c <= 'M'):
            result += c
    return result