def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [char for char in s[40:91] if char in vowels and char > 'a' and (char <= 'x')]