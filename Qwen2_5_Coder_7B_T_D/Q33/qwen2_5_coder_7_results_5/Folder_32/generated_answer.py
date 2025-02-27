def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(45, 76):
        if s[i] in vowels and 'b' < s[i] <= 'z':
            result.append(s[i])
    return result