def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in s[56:96] if char in vowels and ord(char) > ord('&') and (ord(char) <= ord('T'))]