def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[63:79] if char in vowels and 'd' < char <= 'y']