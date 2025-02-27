def return_vowels(s):
    vowels = ['e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'a', 'A']
    return [char for char in s[51:77] if char in vowels and ord(char) > ord('5') and (ord(char) <= ord('='))]