def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[51:77] if char in vowels and ord(char) > 4 and (ord(char) <= 61)]
    return result