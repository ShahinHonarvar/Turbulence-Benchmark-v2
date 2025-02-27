def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(60, 99):
        if s[i] in vowels and 'j' < s[i] <= 'n':
            result.append(s[i])
    return result