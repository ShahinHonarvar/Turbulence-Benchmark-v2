def return_vowels(s):
    vowels = [char for char in s[64:82] if char in 'aeiou' and char > 'P' and (char <= 'z')]
    return vowels