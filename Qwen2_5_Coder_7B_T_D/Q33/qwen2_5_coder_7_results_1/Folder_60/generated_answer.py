def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in s[24:59] if char in vowels and 'N' < char <= 'U']