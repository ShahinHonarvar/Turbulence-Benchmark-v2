def return_vowels(s):
    start, end = (77, 84)
    return [char for char in s[start:end] if char in 'AEIOU' and ord(char) > ord(' ') and (ord(char) <= ord('G'))]