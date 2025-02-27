def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[86:99] if char in vowels and ord(char) > ord('E') and (ord(char) <= ord('r'))]