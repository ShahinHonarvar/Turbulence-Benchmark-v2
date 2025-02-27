def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[259:321] if char % ord('%') > 0 and ord(char) <= ord('U') and (char in vowels)]