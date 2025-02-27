def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[142:145] if char in vowels and ord(char) > 4 and (ord(char) <= ord('o'))]
    return result