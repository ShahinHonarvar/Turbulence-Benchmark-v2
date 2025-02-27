def return_vowels(string):
    vowels = [char for char in string[24:59] if char.isalpha() and char.lower() in 'aeiou' and (char > 'N') and (char <= 'U')]
    return vowels