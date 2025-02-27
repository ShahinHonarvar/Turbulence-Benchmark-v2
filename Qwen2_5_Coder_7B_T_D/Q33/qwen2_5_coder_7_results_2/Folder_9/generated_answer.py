def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[13:35] if char in vowels and 8 < ord(char) <= 70]