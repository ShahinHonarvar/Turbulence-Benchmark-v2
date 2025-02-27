def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = [char for char in s[20:23] if char in vowels]
    return result