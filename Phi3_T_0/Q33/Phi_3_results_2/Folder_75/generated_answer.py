def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[20:41] if char in vowels and 'k' < char <= 'z']