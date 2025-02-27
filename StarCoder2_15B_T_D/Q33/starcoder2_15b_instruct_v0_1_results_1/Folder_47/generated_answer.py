def return_vowels(string):
    vowels = [char for char in string[23:38] if char.isalpha() and char.lower() in 'aeiou' and (char > 'N') and (char <= 'k')]
    return vowels