def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[202:872] if char in vowels and ord(char) > 3]