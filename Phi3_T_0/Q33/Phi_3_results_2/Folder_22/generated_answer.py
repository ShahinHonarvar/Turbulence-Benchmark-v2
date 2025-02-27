def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[56:90] if char in vowels and 'k' < char <= 'z']
    return result