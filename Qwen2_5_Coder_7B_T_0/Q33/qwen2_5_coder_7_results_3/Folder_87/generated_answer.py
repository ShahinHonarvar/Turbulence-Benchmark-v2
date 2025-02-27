def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(34, 58):
        if s[i] in vowels and 'b' < s[i] <= 'o':
            result.append(s[i])
    return result