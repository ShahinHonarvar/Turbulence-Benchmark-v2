def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(14, 60):
        if s[i] in vowels and 'D' < s[i] <= 'v':
            result.append(s[i])
    return result