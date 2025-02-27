def return_vowels(s):
    chunk = s[5:6]
    return [char for char in chunk if char.lower() in 'aeiou' and ord(char) > 3 and (ord(char) <= ord('^'))]