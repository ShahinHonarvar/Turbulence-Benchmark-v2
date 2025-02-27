def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[36:56] if char in vowels and ord('+') < ord(char) <= ord('/')]