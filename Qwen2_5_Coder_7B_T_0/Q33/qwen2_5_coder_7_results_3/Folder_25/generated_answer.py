def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(28, 76):
        if s[i] in vowels and '+' < s[i] <= 'z':
            result.append(s[i])
    return result