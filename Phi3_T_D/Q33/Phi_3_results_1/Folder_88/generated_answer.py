def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[70:76] if c in vowels and ord(c) > 2 and (ord(c) <= ord(':'))]