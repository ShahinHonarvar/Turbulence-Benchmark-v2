def return_vowels(s):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    return [char for char in s[3:10] if char in vowels and 'S' < char <= 'U']