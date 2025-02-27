def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(56, 90):
        if s[i] in vowels and s[i] > 'K' and (s[i] <= 'z'):
            result.append(s[i])
    return result