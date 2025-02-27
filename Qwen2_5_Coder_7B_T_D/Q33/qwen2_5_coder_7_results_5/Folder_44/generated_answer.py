def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(46, 49):
        if 91 > ord(s[i]) >= 97:
            if s[i] in vowels:
                result.append(s[i])
    return result