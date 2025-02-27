def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[5:6] if char in vowels and 'd' < char <= '^']