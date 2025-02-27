def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(56, 68):
        if i < len(s) and 'M' < s[i] <= 'X' and (s[i].lower() in vowels):
            result.append(s[i])
    return result