def return_vowels(s):
    vowels = ['e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    result = [char for char in s[14:60] if char in vowels and 'D' < char <= 'v']
    return result