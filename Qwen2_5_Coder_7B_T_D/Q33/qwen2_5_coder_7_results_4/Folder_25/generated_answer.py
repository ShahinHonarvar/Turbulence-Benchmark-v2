def return_vowels(s):
    vowels = [char for char in s[28:76] if char in 'aeiou' and char > '+' and (char <= 'z')]
    return vowels