def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(22, 82):
        if s[i] in vowels and 'N' < s[i] <= 'o':
            result.append(s[i])
    return result