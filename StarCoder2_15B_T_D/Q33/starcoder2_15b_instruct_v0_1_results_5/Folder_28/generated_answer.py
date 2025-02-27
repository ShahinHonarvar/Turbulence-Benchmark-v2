def return_vowels(string):
    vowels = [char for char in string[41:50] if char.isalpha() and char.lower() in 'aeiou']
    return [char for char in vowels if char.upper() > 'W' and char <= '[']