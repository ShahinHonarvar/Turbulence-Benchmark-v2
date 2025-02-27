def return_vowels(s):
    vowels = [char for char in s[13:35] if char in 'aeiou' and 8 < ord(char) <= ord('F')]
    return vowels