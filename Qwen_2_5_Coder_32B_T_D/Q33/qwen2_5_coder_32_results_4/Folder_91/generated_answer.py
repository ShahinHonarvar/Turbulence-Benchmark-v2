def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[4:8] if char in vowels and 'P' < char <= 'r']
    return result