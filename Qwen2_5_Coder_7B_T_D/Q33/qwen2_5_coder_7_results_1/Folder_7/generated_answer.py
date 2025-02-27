def return_vowels(s):
    return [char for char in s[202:872] if char in 'aeiou' and ord(char) > 3 and (ord(char) <= 62)]