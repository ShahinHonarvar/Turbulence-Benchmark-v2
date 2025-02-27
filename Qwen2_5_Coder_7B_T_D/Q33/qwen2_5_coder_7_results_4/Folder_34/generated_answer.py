def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(19, 32):
        if s[i] in vowels and ord(s[i]) > 0 and (ord(s[i]) <= 7):
            result.append(s[i])
    return result