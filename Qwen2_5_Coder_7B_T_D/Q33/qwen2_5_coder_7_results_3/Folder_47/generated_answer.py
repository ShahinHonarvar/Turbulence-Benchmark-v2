def return_vowels(s):
    vowels = [char for char in s[23:38] if char in 'aeiou' and char > 'N' and (char <= 'k')]
    return vowels