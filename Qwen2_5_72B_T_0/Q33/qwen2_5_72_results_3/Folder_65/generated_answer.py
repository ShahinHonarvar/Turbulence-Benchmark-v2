def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[71:88] if char in vowels and ord(char) > ord('9') and (ord(char) <= ord('P'))]