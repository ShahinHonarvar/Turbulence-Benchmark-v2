def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[273:275] if c in vowels and ord('+') < ord(c) <= ord('o')]