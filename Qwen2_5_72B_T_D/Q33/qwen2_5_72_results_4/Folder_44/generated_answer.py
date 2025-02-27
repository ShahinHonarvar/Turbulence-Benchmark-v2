def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(46, 49):
        if s[i] in vowels and 'Z' < s[i] <= 'p':
            result.append(s[i])
    return result