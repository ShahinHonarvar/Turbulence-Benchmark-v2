def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[142:145]:
        if char in vowels and 4 < ord(char) <= ord('o'):
            result.append(char)
    return result