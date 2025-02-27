def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[1:7] if char in vowels and 'f' < char <= 'j']
    return result