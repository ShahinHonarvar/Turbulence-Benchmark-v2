def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [c for c in s[56:68] if c in vowels and ord(c) > ord('M') and (ord(c) <= ord('X'))]