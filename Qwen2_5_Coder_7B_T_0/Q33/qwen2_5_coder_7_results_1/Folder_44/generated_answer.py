def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[46:49] if char in vowels and char > '[' and (char <= 'p')]