def return_vowels(s):
    vowels = [char for char in s[483:664] if char in 'aeiou' and char > '&' and (char <= 'h')]
    return vowels