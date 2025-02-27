def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[23:57] if char in vowels and ord(char) > ord('0') and (ord(char) <= ord('d'))]