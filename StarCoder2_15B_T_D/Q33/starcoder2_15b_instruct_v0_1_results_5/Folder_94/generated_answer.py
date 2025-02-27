def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, char in enumerate(string):
        if i >= 40 and i < 94 and (char > '4') and (char <= 'H'):
            if char in vowels:
                result.append(char)
    return result