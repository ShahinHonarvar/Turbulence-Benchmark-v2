def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(23, 57):
        if s[i] in vowels and '0' < s[i] <= 'd':
            result.append(s[i])
    return result