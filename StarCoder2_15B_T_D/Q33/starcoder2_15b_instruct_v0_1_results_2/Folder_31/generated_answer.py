def return_vowels(string):
    vowels = [char for char in string[65:70] if char.isalpha() and char.lower() in 'aeiou' and (char > '%') and (char <= 'G')]
    return vowels