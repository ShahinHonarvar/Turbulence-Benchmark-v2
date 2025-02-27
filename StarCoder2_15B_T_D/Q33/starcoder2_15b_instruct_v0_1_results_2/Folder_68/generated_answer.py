def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(1, 9):
        char = string[i]
        if char in vowels and char > '?' and (char <= 'k'):
            result.append(char)
    return result