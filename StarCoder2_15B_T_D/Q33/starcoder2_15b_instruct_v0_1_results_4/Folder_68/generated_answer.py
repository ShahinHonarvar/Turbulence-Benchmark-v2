def return_vowels(string):
    vowels = [char for char in string[1:9] if char.isalpha() and char.lower() in 'aeiou' and (char > '?') and (char <= 'k')]
    return vowels