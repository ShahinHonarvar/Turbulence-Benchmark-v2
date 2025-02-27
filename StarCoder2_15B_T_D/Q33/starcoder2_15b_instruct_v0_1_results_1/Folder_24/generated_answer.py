def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, char in enumerate(string):
        if i >= 23 and i < 57 and (char > '0') and (char <= 'd') and (char in vowels):
            result.append(char)
    return result