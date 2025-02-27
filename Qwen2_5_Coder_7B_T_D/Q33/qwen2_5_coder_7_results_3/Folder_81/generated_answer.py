def return_vowels(s):
    return [char for char in s[20:43] if char in 'aeiou' and ord(char) > 5 and (ord(char) <= ord('M'))]