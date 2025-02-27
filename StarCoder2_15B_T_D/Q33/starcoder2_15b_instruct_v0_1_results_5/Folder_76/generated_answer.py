def return_vowels(string):
    vowels = [char for char in string[495:837] if char.isalpha() and char.lower() in 'aeiou' and (char > 'B') and (char <= 't')]
    return vowels