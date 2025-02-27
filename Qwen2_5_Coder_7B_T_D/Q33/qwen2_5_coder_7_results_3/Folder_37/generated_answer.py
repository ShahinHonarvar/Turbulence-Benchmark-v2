def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(82, 90):
        if s[i] in vowels and 'T' < s[i] <= 'b':
            result.append(s[i])
    return result