def return_vowels(s):
    result = []
    vowels = 'aeiou'
    for i in range(2, 7):
        if s[i] in vowels and '^' < s[i] <= 'd':
            result.append(s[i])
    return result