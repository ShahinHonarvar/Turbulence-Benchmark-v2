def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(464, 574):
        if s[i] in vowels and 'a' < s[i] <= 'g':
            result.append(s[i])
    return result