def return_vowels(string):
    vowels = [char for char in string[3:9] if char.isalpha() and char.lower() in 'aeiou' and (char > 'S') and (char <= 'U')]
    return vowels