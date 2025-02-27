def return_vowels(string):
    vowels = [char for char in string[23:57] if char.isalpha() and char > '0' and (char <= 'd')]
    return vowels