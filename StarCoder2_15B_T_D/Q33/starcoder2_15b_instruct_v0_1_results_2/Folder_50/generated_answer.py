def return_vowels(string):
    vowels = [char for char in string[11:53] if char.isalpha() and char.lower() in 'aeiou']
    return vowels