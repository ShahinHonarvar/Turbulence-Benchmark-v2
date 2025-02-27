def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[28:76] if char in vowels and char > '+' and (char <= 'z')]