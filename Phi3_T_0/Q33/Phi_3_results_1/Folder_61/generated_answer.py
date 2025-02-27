def return_vowels(s):
    vowels = ['e', 'i']
    return [char for char in s[1:4] if char in vowels and 'c' < char <= 'i']