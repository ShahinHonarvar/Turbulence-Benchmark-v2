def return_vowels(string):
    return [char for char in string[77:84] if char.isalpha() and char.lower() in 'aeiou' and (char > '(') and (char <= 'G')]