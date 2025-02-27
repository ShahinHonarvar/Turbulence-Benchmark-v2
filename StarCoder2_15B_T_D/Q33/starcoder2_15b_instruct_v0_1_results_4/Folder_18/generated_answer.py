def return_vowels(string):
    vowels = [char for char in string[528:606] if char.isalpha() and char.lower() in 'aeiou' and (char > 'M') and (char <= 'X')]
    return vowels