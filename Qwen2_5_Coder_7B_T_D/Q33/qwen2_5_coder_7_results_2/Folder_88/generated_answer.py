def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(70, 76):
        if '2' < s[i] <= ':' and s[i] in vowels:
            result.append(s[i])
    return result