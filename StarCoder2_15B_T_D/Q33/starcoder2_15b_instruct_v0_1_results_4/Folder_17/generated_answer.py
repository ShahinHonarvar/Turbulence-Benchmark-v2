def return_vowels(string):
    vowels = [char for char in string[60:99] if char.isalpha() and char.lower() in 'aeiou' and (char > 'j') and (char <= 'n')]
    return vowels