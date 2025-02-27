def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(29, 73):
        if s[i] > '#' and s[i] <= '(' and (s[i].lower() in vowels):
            result.append(s[i])
    return result