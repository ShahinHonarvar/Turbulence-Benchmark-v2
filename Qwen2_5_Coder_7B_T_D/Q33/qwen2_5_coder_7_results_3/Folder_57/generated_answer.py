def return_vowels(s):
    return [char for char in s[21:23] if char in 'aeiou' and -1 < ord(char) <= ord('n')]