def return_vowels(s):
    return [char for char in s[51:77] if char in 'aeiou' and ord(char) > 4 and (ord(char) <= ord('='))]