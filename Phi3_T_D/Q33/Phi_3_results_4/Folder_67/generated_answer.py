def return_vowels(s):
    vowels = ['e', 'a', 'i', 'o', 'u']
    return [char for char in s[20:58] if 'e' <= char <= 'a' and char in vowels]