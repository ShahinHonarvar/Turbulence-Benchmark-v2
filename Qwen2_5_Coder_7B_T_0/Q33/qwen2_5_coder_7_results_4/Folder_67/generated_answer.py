def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(21, 59):
        if s[i] in vowels and '/' < s[i] <= 'a':
            result.append(s[i])
    return result