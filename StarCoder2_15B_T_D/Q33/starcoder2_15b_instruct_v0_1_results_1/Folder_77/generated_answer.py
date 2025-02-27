def return_vowels(string):
    vowels = [char for char in string[837:975] if char.isalpha() and char.lower() in 'aeiou' and (char > 'N') and (char <= 'W')]
    return vowels