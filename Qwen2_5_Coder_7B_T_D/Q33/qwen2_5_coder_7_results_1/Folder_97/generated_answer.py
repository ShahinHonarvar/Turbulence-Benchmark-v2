def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(328, 455):
        if 32 < ord(s[i]) <= 122 and s[i] in vowels:
            result.append(s[i])
    return result