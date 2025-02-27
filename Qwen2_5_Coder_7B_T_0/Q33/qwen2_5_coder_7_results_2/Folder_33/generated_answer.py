def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(163, 771):
        if s[i] in vowels and ':' < s[i] <= 'E':
            result.append(s[i])
    return result