def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, char in enumerate(string):
        if i >= 12 and i < 39 and (char in vowels) and (';' < char <= '|'):
            result.append(char)
    return result