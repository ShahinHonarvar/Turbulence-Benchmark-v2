def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in s[13:35] if char in vowels and 'I' < char <= 'F']