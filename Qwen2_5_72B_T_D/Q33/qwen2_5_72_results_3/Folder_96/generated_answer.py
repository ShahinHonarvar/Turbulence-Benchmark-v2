def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(77, 84):
        if s[i] in vowels and '(' < s[i] <= 'G':
            result.append(s[i])
    return result