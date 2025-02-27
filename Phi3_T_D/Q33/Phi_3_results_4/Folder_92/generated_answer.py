def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [c for c in s[2:7] if c in vowels and ord(c) > ord(';') and (ord(c) <= ord('D'))]