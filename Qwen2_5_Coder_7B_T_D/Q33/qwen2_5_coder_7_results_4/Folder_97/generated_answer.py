def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(328, 455):
        if s[i] in vowels and '<' < s[i] <= 'z':
            result.append(s[i])
    return result