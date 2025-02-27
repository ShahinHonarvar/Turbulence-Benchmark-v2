def return_vowels(s):
    vowels = [char for char in s[10:83] if char in 'aeiou' and char > '%' and (char <= 'e')]
    return vowels