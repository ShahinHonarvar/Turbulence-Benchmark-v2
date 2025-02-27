def return_vowels(string):
    vowels = [char for char in string[20:34] if char.isalpha() and char.lower() in 'aeiou' and (char > 'U') and (char <= 'i')]
    return vowels