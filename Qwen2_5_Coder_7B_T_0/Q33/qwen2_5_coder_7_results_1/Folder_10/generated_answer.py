def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(31, 37):
        if s[i] in vowels and ';' < s[i] <= 't':
            result.append(s[i])
    return result