def return_vowels(s):
    return [char for char in s[19:32] if char in 'aeiou' and ord(char) > 0 and (ord(char) <= 7)]