def return_vowels(s):
    return [char for char in s[23:57] if char in 'aeiou' and ord(char) > ord('0') and (ord(char) <= ord('d'))]