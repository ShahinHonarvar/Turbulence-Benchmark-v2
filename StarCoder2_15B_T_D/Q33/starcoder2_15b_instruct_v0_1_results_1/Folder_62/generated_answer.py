def return_vowels(string):
    vowels = [char for char in string[14:60] if char.isalpha() and char.lower() in 'aeiou' and (char > 'D') and (char <= 'v')]
    return vowels