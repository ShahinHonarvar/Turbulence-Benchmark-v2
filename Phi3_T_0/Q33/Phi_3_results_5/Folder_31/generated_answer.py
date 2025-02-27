def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in s[65:70] if char in vowels and ord(char) > ord('%') and (ord(char) <= ord('G'))]