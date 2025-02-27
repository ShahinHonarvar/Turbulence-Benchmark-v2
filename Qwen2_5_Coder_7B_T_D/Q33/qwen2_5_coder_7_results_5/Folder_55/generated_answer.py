def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[1:5] if char in vowels and char > '!' and (char <= 'j')]