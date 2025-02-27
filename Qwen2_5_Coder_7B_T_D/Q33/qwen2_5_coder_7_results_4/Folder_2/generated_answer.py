def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(170, 645):
        char = s[i]
        if char in vowels and 'E' < char <= '~':
            result.append(char)
    return result