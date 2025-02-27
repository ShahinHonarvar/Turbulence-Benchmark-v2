def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[5:6] if char in vowels and ord(char) > ord('3') and (ord(char) <= ord('^'))]
    return result