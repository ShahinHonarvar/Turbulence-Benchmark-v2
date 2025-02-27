def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[5:6] if char in vowels and ord(char) > 3 and (ord(char) <= ord('^'))]
    return result