def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[13:35] if char in vowels and ord(char) > 8 and (ord(char) <= ord('F'))]