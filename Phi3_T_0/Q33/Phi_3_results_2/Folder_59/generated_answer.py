def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[8:9] if char in vowels and 'y' < char <= 's']
    return result