def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[19:32]:
        if char in vowels and ord(char) > 0 and (ord(char) <= 7):
            result.append(char)
    return result