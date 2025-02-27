def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[44:95] if 'a' < c <= 'z' and c in vowels]