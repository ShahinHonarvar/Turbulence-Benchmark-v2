def return_vowels(string):
    vowels = [char for char in string[37:57] if char.isalpha() and char.lower() in 'aeiou' and (char > '*') and (char <= 'P')]
    return vowels