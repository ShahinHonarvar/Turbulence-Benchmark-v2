def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(43, 70):
        if s[i] in vowels and '*' < s[i] <= 'b':
            result.append(s[i])
    return result