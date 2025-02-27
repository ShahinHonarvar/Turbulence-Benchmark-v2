def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, char in enumerate(string):
        if i >= 641 and i < 872 and (char in vowels) and (char > '>') and (char <= 'q'):
            result.append(char)
    return result