def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[9:96] if char in vowels and 'r' < char <= 'b']