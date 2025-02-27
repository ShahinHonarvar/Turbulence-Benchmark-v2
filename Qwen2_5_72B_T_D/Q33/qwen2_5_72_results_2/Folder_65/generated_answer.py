def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[71:88] if char in vowels and 9 < ord(char) <= ord('P')]