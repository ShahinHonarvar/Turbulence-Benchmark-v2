def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [c for c in s[40:94] if c in vowels and ord(c) > ord('4') and (ord(c) <= ord('H'))]