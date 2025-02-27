def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(142, 145):
        if s[i] in vowels and 4 < ord(s[i]) <= ord('o'):
            result.append(s[i])
    return result