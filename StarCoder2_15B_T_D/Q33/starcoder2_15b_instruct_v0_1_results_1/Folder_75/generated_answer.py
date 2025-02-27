def return_vowels(string):
    vowels = 'AEIOU'
    result = []
    for i, char in enumerate(string):
        if i >= 20 and i < 41 and (char in vowels) and (char > 'K') and (char <= 'Z'):
            result.append(char)
    return result