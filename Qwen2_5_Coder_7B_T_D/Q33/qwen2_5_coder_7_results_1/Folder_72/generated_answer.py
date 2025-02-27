def return_vowels(s):
    vowels = [char for char in s[37:57] if char in 'aeiou' and char > '*' and (char <= 'P')]
    return vowels