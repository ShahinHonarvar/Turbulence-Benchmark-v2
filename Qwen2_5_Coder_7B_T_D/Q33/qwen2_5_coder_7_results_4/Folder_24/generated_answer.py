def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[23:57] if char in vowels and 0 < ord(char) <= ord('d')]