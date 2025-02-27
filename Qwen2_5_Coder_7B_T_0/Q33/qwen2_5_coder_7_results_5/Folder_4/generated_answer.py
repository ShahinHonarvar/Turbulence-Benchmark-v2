def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[40:91] if char in vowels and char > 'A' and (char <= 'x')]
    return result