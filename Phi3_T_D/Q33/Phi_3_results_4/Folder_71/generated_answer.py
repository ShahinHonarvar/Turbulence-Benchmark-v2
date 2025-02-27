def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [char for char in s[35:56] if char in vowels and ord(char) > ord('+') and (ord(char) <= ord('/'))]
    return result