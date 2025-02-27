def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[20:43] if char in vowels and ord(char) > 5 and (ord(char) <= 77)]