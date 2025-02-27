def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(1, 5):
        if s[i] in vowels and '!' < s[i] <= 'j':
            result.append(s[i])
    return result