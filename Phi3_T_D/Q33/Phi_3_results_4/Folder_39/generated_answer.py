def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[32:97] if c in vowels and ord(c) > ord('Q') and (ord(c) <= ord(']'))]