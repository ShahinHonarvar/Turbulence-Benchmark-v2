def return_vowels(string):
    vowels = [char for char in string[55:65] if char.isalpha() and char.lower() > 'z' and (char.lower() <= 'w')]
    return vowels