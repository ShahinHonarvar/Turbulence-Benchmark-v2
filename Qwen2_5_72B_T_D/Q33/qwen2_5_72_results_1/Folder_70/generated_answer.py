def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(171, 402):
        if i < len(s) and 'I' < s[i] <= 'k' and (s[i] in vowels):
            result.append(s[i])
    return result