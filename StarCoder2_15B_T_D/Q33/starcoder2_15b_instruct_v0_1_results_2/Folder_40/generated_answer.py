def return_vowels(string):
    vowels = [char for char in string[2:7] if char.isalpha() and char.lower() in 'aeiou' and (char > '^') and (char <= 'd')]
    return vowels