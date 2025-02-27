def return_vowels(string):
    vowels = [char for char in string[32:97] if char.isalpha() and char > 'Q' and (char <= ']')]
    return vowels