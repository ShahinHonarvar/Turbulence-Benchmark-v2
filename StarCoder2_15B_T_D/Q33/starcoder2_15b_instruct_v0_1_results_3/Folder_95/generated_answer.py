def return_vowels(string):
    vowels = [char for char in string[32:61] if char in 'AEIOU' and char > '?' and (char <= 'P')]
    return vowels