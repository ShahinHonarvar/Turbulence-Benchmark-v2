def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[24:64] if char in vowels and 'f' < char <= 'h']