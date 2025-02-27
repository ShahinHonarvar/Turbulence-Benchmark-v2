def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(86, 99):
        if s[i] in vowels and 'E' < s[i] <= 'r':
            result.append(s[i])
    return result