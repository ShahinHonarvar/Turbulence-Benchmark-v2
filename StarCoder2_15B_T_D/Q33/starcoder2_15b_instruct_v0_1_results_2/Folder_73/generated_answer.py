def return_vowels(string):
    result = []
    vowels = 'aeiou'
    for i, char in enumerate(string):
        if i >= 47 and i < 89 and (char in vowels) and (char > '@') and (char <= 'n'):
            result.append(char)
    return result