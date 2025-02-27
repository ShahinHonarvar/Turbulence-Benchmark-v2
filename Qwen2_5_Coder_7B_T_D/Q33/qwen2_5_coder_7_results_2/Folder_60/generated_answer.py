def return_vowels(s):
    vowels = [char for char in s[24:59] if char in 'AEIOU' and char > 'N' and (char <= 'U')]
    return vowels