def return_vowels(string):
    return [char for char in string[74:96] if char.isalpha() and char.lower() in 'aeiou' and (char > 'I') and (char <= 'X')]