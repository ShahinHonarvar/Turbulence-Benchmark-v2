def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[483:664] if char in vowels and ord(char) > ord('&') and (ord(char) <= ord('h'))]