def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, char in enumerate(string):
        if char in vowels and i >= 40 and (i < 91) and (char > 'A') and (char <= 'x'):
            result.append(char)
    return result