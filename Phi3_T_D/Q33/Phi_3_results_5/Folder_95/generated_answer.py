def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [char for char in s[32:61] if char in vowels and char <= 'P']
    return result