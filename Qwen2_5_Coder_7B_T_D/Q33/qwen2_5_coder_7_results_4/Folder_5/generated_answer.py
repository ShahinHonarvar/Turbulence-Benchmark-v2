def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 44 <= i < 95 and char in vowels and (5 < ord(char) < ord('<'))]
    return result