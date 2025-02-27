def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in s[20:41] if char in vowels and 'K' < char <= 'Z']