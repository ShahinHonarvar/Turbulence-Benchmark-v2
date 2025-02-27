def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in s[3:8] if char > ';' and char <= 'D' and (char in vowels)]