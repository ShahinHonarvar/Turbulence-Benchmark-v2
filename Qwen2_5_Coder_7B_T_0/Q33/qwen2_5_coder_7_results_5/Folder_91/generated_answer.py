def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(4, 8):
        if s[i] in vowels and 'P' < s[i] <= 'r':
            result.append(s[i])
    return result