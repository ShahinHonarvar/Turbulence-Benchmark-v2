def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[70:76] if char in vowels and ord(char) > 2 and (ord(char) <= ord(':'))]