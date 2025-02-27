def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = [char for char in s[23:38] if char in vowels and 'n' < char <= 'k']
    return result