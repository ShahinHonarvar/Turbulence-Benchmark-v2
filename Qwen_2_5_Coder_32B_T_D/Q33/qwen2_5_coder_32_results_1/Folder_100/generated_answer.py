def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[23:75] if char in vowels and 'L' < char <= 'd']