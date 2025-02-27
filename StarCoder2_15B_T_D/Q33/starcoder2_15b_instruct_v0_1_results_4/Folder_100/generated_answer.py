def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, char in enumerate(string):
        if i >= 23 and i < 75 and (char in vowels) and (char > 'L') and (char <= 'd'):
            result.append(char)
    return result