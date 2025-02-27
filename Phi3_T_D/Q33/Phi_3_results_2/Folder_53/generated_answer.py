def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[27:57] if c in vowels and 'o' < c <= 'w']