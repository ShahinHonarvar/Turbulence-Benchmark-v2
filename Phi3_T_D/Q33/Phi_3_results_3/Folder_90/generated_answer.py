def return_vowels(s):
    vowels = ['i', 'o', 'u']
    return [c for c in s[142:145] if c in vowels and ord(c) > ord('4') and (ord(c) <= ord('o'))]