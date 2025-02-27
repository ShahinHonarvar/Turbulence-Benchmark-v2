def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(19, 32):
        if i < len(s) and '0' < s[i] <= '7' and (s[i] in vowels):
            result.append(s[i])
    return result