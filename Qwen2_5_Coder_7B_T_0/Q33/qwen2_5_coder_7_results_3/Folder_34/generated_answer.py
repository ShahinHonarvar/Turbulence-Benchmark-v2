def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(19, 32):
        if s[i] in vowels and '0' < s[i] <= '7':
            result.append(s[i])
    return result