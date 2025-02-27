def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(20, 41):
        if i < len(s) and s[i] in vowels and ('k' < s[i] <= 'z'):
            result.append(s[i])
    return result