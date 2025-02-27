def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[37:57] if 'a' <= char <= 'P' and char in vowels]
    return result