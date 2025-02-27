def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(21, 23):
        if s[i] in vowels and -'a' < ord(s[i]) <= ord('n'):
            result.append(s[i])
    return result