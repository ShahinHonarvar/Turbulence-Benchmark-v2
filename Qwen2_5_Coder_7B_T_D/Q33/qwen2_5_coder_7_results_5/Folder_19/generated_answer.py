def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[51:77] if char in vowels and ord(char) > 4 and (ord(char) <= 61)]
    return result