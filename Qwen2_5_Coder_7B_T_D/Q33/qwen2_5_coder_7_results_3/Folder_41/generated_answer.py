def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(71, 81):
        if 62 < ord(s[i]) <= 85:
            if s[i].lower() in vowels:
                result.append(s[i])
    return result