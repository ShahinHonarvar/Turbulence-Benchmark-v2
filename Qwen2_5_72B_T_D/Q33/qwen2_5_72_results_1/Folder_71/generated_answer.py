def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(36, 56):
        if i < len(s) and s[i] in vowels and ('+' < s[i] <= '/'):
            result.append(s[i])
    return result