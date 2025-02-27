def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(47, 89):
        if s[i] in vowels and '@' < s[i] <= 'n':
            result.append(s[i])
    return result