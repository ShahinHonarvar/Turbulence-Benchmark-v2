def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(171, 402):
        if s[i] in vowels and 'I' < s[i] <= 'k':
            result.append(s[i])
    return result