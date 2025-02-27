def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(74, 96):
        if s[i] in vowels and 'I' < s[i] <= 'X':
            result.append(s[i])
    return result