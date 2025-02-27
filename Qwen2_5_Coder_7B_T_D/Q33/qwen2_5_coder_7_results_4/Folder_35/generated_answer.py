def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(483, 664):
        if 97 <= ord(s[i]) <= 104 and s[i] in vowels:
            result.append(s[i])
    return result