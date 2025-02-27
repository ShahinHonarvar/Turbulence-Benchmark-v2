def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in s[13:35] if '8' < char <= 'F' and char in vowels]