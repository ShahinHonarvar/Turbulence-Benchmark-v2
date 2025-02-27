def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in s[604:949] if char in vowels and char > 'N' and (char <= 'U')]