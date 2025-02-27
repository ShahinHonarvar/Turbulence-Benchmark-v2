def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, char in enumerate(string):
        if i >= 483 and i < 664 and (char in vowels) and (char > '&') and (char <= 'h'):
            result.append(char)
    return result