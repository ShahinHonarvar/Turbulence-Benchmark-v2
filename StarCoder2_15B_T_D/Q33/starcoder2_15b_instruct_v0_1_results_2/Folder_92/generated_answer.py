def return_vowels(string):
    vowels = [char for char in string[3:8] if char.isalpha() and char.lower() in 'aeiou' and (char > ';') and (char <= 'D')]
    return vowels