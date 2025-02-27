def return_vowels(s):
    vowels = ['S', 'T', 'U']
    return [char for char in s[3:9] if char in vowels and 'S' < char <= 'U']