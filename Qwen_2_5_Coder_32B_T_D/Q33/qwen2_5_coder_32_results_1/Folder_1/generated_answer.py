def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[24:64] if char in vowels and 'F' < char <= 'h']
    return result