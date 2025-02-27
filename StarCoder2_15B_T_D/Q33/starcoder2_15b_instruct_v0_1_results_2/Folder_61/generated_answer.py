def return_vowels(string):
    return [char for char in string[1:4] if char.isalpha() and char.lower() in 'aeiou' and (char > 'C') and (char <= 'I')]