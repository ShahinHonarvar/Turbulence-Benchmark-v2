def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(85, 99):
        if s[i] in vowels and '/' < s[i] <= 'n':
            result.append(s[i])
    return result