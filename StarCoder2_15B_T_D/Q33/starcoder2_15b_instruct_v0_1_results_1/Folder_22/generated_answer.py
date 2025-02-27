def return_vowels(string):
    vowels = [char for char in string[56:90] if char.isalpha() and char.lower() > 'k' and (char.lower() <= 'z')]
    return vowels