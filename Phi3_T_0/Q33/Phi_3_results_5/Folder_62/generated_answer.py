def return_vowels(s):
    vowels = ['e', 'i', 'o', 'u']
    return [char for char in s[14:60] if char in vowels and 'd' < char <= 'v']