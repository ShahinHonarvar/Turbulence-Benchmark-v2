def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(8, 9):
        if s[i] in vowels and 'Y' < s[i] <= 's':
            result.append(s[i])
    return result