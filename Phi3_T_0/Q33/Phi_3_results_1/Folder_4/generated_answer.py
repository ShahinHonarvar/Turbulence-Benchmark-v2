def return_vowels(s):
    vowels = ['e', 'i', 'o', 'u']
    return [char for char in s[40:91] if char in vowels and 'a' < char <= 'x']